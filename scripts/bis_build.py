def dfs_util(item_id, item_dict, itemUsageDict, visited, candidates, selection):

    #A CANDIDATE WAS PICKED FROM CRITERIA AND ITS THE ONE WE SHOULD END WITH
    if selection != None:
        return 

    #IF IT IS STILL A SECONDARY ITEM
    if item_dict[item_id].has_key("into"):
        for item in item_dict[item_id]["into"]:
            if item not in visited:
                #THE ITEM HAS NOT BEEN VISITED AND ALL POSSIBLE ROUTES SHOULD BE EXAMINED
                visited.add(item_id)
                dfs_util(item, item_dict, visited)
            else:
                #THE ITEM HAS BEEN EXAMINED IN THE PAST. GOOD TO BREAK FROM HERE BECAUSE THAT ROUTE WILL PROB LEAD TO THE SAME
                break

    #REACHED THE END. NEEDS SOME CRITERIA.
    else:
        #Meets the basic criteria of being over 50% win Rate(good chance of winning with this item on)
        if itemUsageDict["totalCount"] > 200 and itemUsageDict["winRatio"] >= 0.55:
            selection = item_id
        else:
            candidates.append(item_id)
        return

def dfs(item_id, item_dict, itemUsageDict, visited = set(), candidates = list(), selection = None):
    dfs_util(item_id, item_dict, itemUsageDict, visited, candidates, selection)

    if selection != None:
        return item_id

    else:
        #SEARCHES FOR THE MAX INSTANCE WITH A GRADUAL DESCENT STEP WITH CRITERIA
        return gradual_descent(candidates, itemUsageDict)

def gradual_descent(candidates, itemUsageDict, step = 0.02, win_epoch  = 0.55, occurence_epoch = 200, max_iter = 5000):
    while max_iter != 0:
        priority_list = list()

        for candidate in candidates:
            if itemUsageDict[candidate]["totalCount"] > occurence_epoch and itemUsageDict[candidate]["winRatio"]:
                priority_list.append(candidate)

        if len(priority_list) != 0:
            #SCORE ITEMS
            if len(priority_list) == 1:
                #base case
                return priority_list[0]
            else:
                return max(score(priority_list, sum([data["totalCount"] for item, data in itemUsageDict.items()]), itemUsageDict, 1.2), key = lambda x: x[1])[0]
        else:
            win_epoch -= win_epoch *step; occurence_epoch -= occurence_epoch * step; max_iter -= 1 


    return

def score(priority_list, totalItemCount, itemUsageDict, threshold):
    scored = list()
    for item in priority_list:
        scored.append((item, itemUsageDict[item]["winRatio"] * (itemUsageDict[item]["totalCount"]/ totalItemCount), threshold))
    return scored


def generate_build(item_dict: dict(dict), itemUsageDict: dict(dict), championName: str, currentBuild = set()) -> list:
    i = 0 
    for itemId in itemUsageDict[championName].keys():
        #SELECT THE NEXT ITEM, ORDERED BY HIGHEST WIN RATE
        if i == 6:
            break

        previous_length = len(currentBuild)
        currentBuild.add(dfs(itemId, item_dict, itemUsageDict[championName]))

        if previous_length != len(currentBuild):
            i += 1

    return currentBuild
    