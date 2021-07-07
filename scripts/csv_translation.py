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
    



if __name__ == "__main__":
    translateCSV("src/queries/itemWInUsage.csv","src/json/itemWinUsage.json", 0, 1, ["itemName", "winCount", "totalCount", "winRatio"])



    
