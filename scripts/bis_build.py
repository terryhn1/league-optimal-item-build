import json
import time
from collections import defaultdict
import pandas
from numpy.lib.arraysetops import unique

from numpy.lib.shape_base import take_along_axis

def dfs_util(item_id, item_dict, itemUsageDict, visited, candidates, selection, unique_tags, current_tags):
    """The recursive function for DFS. Checks for visited nodes and cancels recursion if a similar item path has been encountered.
    If a similar item path has been discovered, then its best to consider that the way will lead to the same item.
    An inherent problem with this function is that one item can lead to multiple paths that can be optimal builds.
    However, this problem is fixed by gradual descent"""

    visited.add(item_id)
    #A CANDIDATE WAS PICKED FROM CRITERIA AND ITS THE ONE WE SHOULD END WITH
    if len(selection) == 1:
        return 

    #IF IT IS STILL A SECONDARY ITEM
    if "into" in item_dict[item_id]:
        for item in item_dict[item_id]["into"]:
            if item not in visited:
                #THE ITEM HAS NOT BEEN VISITED AND ALL POSSIBLE ROUTES SHOULD BE EXAMINED
                dfs_util(item, item_dict,itemUsageDict, visited, candidates, selection, unique_tags, current_tags)
            else:
                #THE ITEM HAS BEEN EXAMINED IN THE PAST. GOOD TO BREAK FROM HERE BECAUSE THAT ROUTE WILL PROB LEAD TO THE SAME
                return

    #REACHED THE END. NEEDS SOME CRITERIA.
    else:
       #ORNN IS A SPECIAL CASE IN LEAGUE. TAKE OUT HIS ITEMS BECAUSE THEY DONT FIT THE GENERAL PLAY
        if "requiredAlly" in item_dict[item_id] and "from" in item_dict[item_id]:
            item_id = item_dict[item_id]["from"][0]

        if item_id in itemUsageDict:
             #Meets the basic criteria of being over 55% win Rate(good chance of winning with this item on)
            if itemUsageDict[item_id]["totalCount"] > 200 and itemUsageDict[item_id]["winRatio"] >= 0.55:
                for tag in unique_tags:
                    if tag in item_dict[item_id]["tags"] and tag in current_tags:
                        return
                    elif tag in item_dict[item_id]["tags"] and tag not in current_tags:

                        current_tags.add(tag)

                selection.add(item_id)    
                return

            elif itemUsageDict[item_id]["totalCount"] > 10:
                candidates.append(item_id)
        return

def dfs(item_id, item_dict, itemUsageDict, visited = set(), candidates = list(), selection = set(), unique_tags = set(), current_tags = set()):
    """Uses the DFS_Util function in order to compute for the candidate selection. If the selection is empty, then it resorts to
    using the gradual descent algorithm to figure out the best candidate out of those candidates that did not meet the strict """
    dfs_util(item_id, item_dict, itemUsageDict, visited, candidates, selection, unique_tags, current_tags)

    if len(selection) != 0:
        return selection.pop()
    else:
        return -1

def gradual_descent(candidates, itemUsageDict, step = 0.01, win_epoch  = 0.55, occurence_epoch = 150, max_iter = 500):
    """Gradual descent attempts to solve the problem of having too strict a condition in the original selection. If no items are found at the primary search,
    gradual descent steps down with a focus of balancing the occurences met and wins. By doing so, we can achieve a local maxima. 
    If max_iter is reached, then the item with the best win ratio is chosen. We can look at this as exploration into the future as this item may be used more often later."""

    if len(candidates) == 1:
        best_candidate = candidates[0]
        candidates.remove(best_candidate)
        return best_candidate

    while max_iter != 0:
        priority_list = list()
        for candidate in candidates:
            if itemUsageDict[candidate]["totalCount"] > occurence_epoch and itemUsageDict[candidate]["winRatio"]:
                priority_list.append(candidate)
        
        if len(priority_list) != 0:
            #SCORE ITEMS
            if len(priority_list) == 1:
                #base case
                best_candidate = priority_list[0]
                candidates.remove(priority_list[0])
                return best_candidate
            else:
                best_candidate = max(score(priority_list, sum([data["totalCount"] for item, data in itemUsageDict.items()]), itemUsageDict, 1.2), key = lambda x: x[1])[0]
                candidates.remove(best_candidate)
                return best_candidate
                
        else:
            win_epoch -= win_epoch *step; occurence_epoch -= occurence_epoch * step; max_iter -= 1 


    return -1

def score(priority_list, totalItemCount, itemUsageDict, threshold):
    """Judges the candidates from the given data to see if """
    scored = list()
    for item in priority_list:
        scored.append((item, itemUsageDict[item]["winRatio"] * (itemUsageDict[item]["totalCount"]/ totalItemCount) * threshold))
    return scored


def generate_build(item_dict: dict, itemUsageDict: dict, championName: str, currentBuild: set) -> list:
    """Takes in the entire item.csv and the itemUsageDict generated by SQL. ItemUsageDict is ordered by championName while the item dict is ordered by item id.
    This function attempts to fulfill all 6 slots for the build(excluding the trinket) by iterating through all items and relying on """
    candidates = list()
    current_tags = set()
    unique_tags = set(["Boots", "Mythic"])
    for itemId in itemUsageDict[championName].keys():
        #SELECT THE NEXT ITEM, ORDERED BY HIGHEST WIN RATE
        if len(currentBuild) == 6:
            break
  
        new_item = dfs(itemId, item_dict, itemUsageDict[championName], candidates = candidates, unique_tags = unique_tags, current_tags = current_tags)
        if new_item != -1:
            currentBuild.add(item_dict[new_item]["name"])

    while len(currentBuild) != 6 and len(candidates) != 0: # the 0 case is to prevent infinite looping
        best_candidate = gradual_descent(candidates, itemUsageDict[championName])
        #Prevention of having two unique items in the same build
        if best_candidate != -1:
            check = list()
            for tag in unique_tags:
                if tag in item_dict[best_candidate]["tags"] and tag not in current_tags:
                    current_tags.add(tag)
                    check.append(True)
                elif tag in item_dict[best_candidate]["tags"] and tag in current_tags:
                    check.append(False)

            if all(check): currentBuild.add(item_dict[best_candidate]["name"])
    return currentBuild

def csvBuild(item_file, itemWin_file):
    with open(item_file) as items:
        with open(itemWin_file) as itemUsageDict:
            totalItems = json.load(items); itemUsage = json.load(itemUsageDict)
            container = defaultdict(list)
            for key in itemUsage.keys():
                currentBuild = list(generate_build(totalItems["data"], itemUsage, key, set()))
                while len(currentBuild) != 6:
                    currentBuild.append('N/A')
                container["championName"].append(key)
                for i, item in enumerate(currentBuild, start = 1):
                    container["item" + str(i)].append(item)

            df = pandas.DataFrame(data = container)
            df.to_csv('src/csv/itemBIS.csv', index = None)
    


if __name__ == "__main__":
    csvBuild('src/json/item.json', 'src/json/itemWinUsage.json')