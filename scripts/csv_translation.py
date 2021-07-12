import numpy as np
from collections import defaultdict
import json


def translateCSV(path: str,dest: str, primary_key: int, secondary_key: int, inner_keys: list)-> None:
    csv_file = np.genfromtxt(path, delimiter = ",", dtype = str, skip_header = 1)
    container = defaultdict(dict)

    #ITERATE THROUGH ALL ROWS
    for i in range(csv_file.shape[0]):
        container[csv_file[i][primary_key]][csv_file[i][secondary_key]] = dict()
        #SELECT KEYS NECESSARY FOR EACH COLUMN
        for j in range(len(inner_keys)):
            container[csv_file[i][primary_key]][csv_file[i][secondary_key]][inner_keys[j]] = csv_file[i][j+2] if testType(csv_file[i][j+2]) == 0 else int(csv_file[i][j+ 2]) if testType(csv_file[i][j+2]) == 1 else float(csv_file[i][j+2])

    with open(dest, 'w') as json_file:
        json.dump(container, json_file)


def testType(s: str):
    try:
        float(s)
        #1 stands for just an integer, 2 stands for float
        return 1 if s.isnumeric() else 2
    except ValueError:
        return 0 #0 means string

def csvItemMatchup():
    item_matchup = np.genfromtxt('src/queries/matches20.csv', dtype = str, delimiter = ",")
    fullItems = open('src/json/item.json', 'r')
    itemHashMap = open('src/json/itemHashMap.json', 'r')
    json_file = json.load(fullItems)
    json_file2 = list(json.load(itemHashMap))
    ignored_items = set([2055, 2003, 2031, 2033, 3330, 3340, 3363, 3364, 2138,2139, 2140, 3400, 1054, 1055, 1056, 1035, 1039, 1083, 2010, 2403])
    ignored_items = {json_file["data"][str(element)]["name"] for element in ignored_items}

    top6 = dict()
    for matchup in item_matchup[1:]:
        top6[matchup[0]] = sorted([(json_file["data"][json_file2[i]]["name"], element) for i,element in enumerate(matchup[3:], start = 0) if json_file["data"][json_file2[i]]["name"] not in ignored_items], key = lambda x: float(x[1]), reverse = True)[:6]
    
    for key, value in top6.items():
        print(key)
        print(value)
    
    fullItems.close()
    itemHashMap.close()

def roleTranslatioGeneralizer():
    pass
        


if __name__ == "__main__":
    #translateCSV("src/queries/itemWInUsage.csv","src/json/itemWinUsage.json", 0, 1, ["itemName", "winCount", "totalCount", "winRatio"])
    csvItemMatchup()



    
