import requests
import pymysql as sql
import time
import numpy as np
import json
import pandas
from collections import defaultdict
from bag import Bag

#Time Module is used for to delay the request calls to make sure that requests are spaced out and there are no Request Errors due to Riot API rules
#Riot API Rule: 20 requests/sec


#CONSTANTS
GRANDMASTER_ENDPOINT = "https://na1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5"
CHALLENGER_ENDPOINT = "https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
MASTER_ENDPOINT = "https://na1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5"
SUMMONERS_ENDPOINT = "https://na1.api.riotgames.com/lol/summoner/v4/summoners"
PUUID_MATCHES_ENDPOINT = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid"
MATCHID_MATCHES_ENDPOINT = "https://americas.api.riotgames.com/lol/match/v5/matches"
TIMELINE = "timeline" #appended after the match ID if requested


#GRANDMASTER REQUEST
# grandmaster = requests.get(url = GRANDMASTER_ENDPOINT, params= {'api_key': API_KEY})
# grandmaster_data = grandmaster.json()
# with open("grandmaster.json", 'w') as json_file: 
#     json.dump(grandmaster_data, json_file)
#     print("request ok")


#CHALLENGER REQUEST
# challenger = requests.get(url = CHALLENGER_ENDPPINT, params = {"api_key": API_KEY})
# challenger_data = challenger.json()
# with open("challenger.json", 'w') as json_file:
#     json.dump(challenger_data, json_file)
#     print("request ok")

#MASTER REQUEST
# master = requests.get(url = MASTER_ENDPOINT, params = {"api_key": API_KEY})
# if master.status_code == 200:
#     master_data = master.json()
#     with open("src/json/master.json", 'w') as json_file:
#         json.dump(master_data, json_file)
#         print("request ok")


#PLAYER PARSING
def tier_data():
    with open('src/json/grandmaster.json', 'r')  as json_file1:
        with open('src/json/challenger.json', 'r') as json_file3:
            with open('src/json/master.json' ,'r') as json_file4:
                with open('src/json/playerv2.json', 'w') as json_file2:
                    player_json = {"entries": []}
                    for i, entry in enumerate(json.load(json_file4)["entries"]):
                        if entry["leaguePoints"] < 100:
                            continue
                        summoner = requests.get(url= SUMMONERS_ENDPOINT + "/" + entry["summonerId"], params = {"api_key": API_KEY})
                        summoner_data = summoner.json()
                        print(summoner.status_code, i)
                        if summoner.status_code == 200:
                            extractedPlayer = {"summonerId": entry["summonerId"], "summonerName": entry["summonerName"], "puuid": summoner_data["puuid"]}
                            player_json["entries"].append(extractedPlayer)
                            print("successful")
                        else:
                            print("unsuccessful")
                        time.sleep(3)
                    oldVer = json.load(open('src/json/player.json', 'r'))
                    player_json["entries"].extend(oldVer["entries"])
                    json.dump(player_json, json_file2)
                    for i, entry in enumerate(grandmaster_data["entries"]):
                        summoner = requests.get(url = SUMMONERS_ENDPOINT + "/" + entry["summonerId"], params = {'api_key': API_KEY})
                        summoner_data = summoner.json()
                        print(summoner.status_code,i)
                        if summoner.status_code == 200:
                            extractedPlayer = {"summonerId": entry["summonerId"], "summonerName": entry["summonerName"], "puuid": summoner_data["puuid"]}
                            player_json["entries"].append(extractedPlayer)
                            print("successful add")
                        else:
                            print("unsuccessful appenditure")
                        time.sleep(3)
                    for i, entry in enumerate(challenger_data["entries"]):
                        summoner = requests.get(url = SUMMONERS_ENDPOINT + "/" + entry["summonerId"], params = {'api_key': API_KEY})
                        summoner_data = summoner.json()
                        print(summoner.status_code, i)
                        if summoner.status_code == 200:
                            extractedPlayer = {"summonerId": entry["summonerId"], "summonerName": entry["summonerName"], "puuid": summoner_data["puuid"]}
                            player_json["entries"].append(extractedPlayer)
                            print("successful add")
                        else:
                            print("unsuccessful apprenditure")
                        time.sleep(3)

# MATCH RESULTS
def match_result():
    with open('src/json/playerv2.json', 'r') as json_file:
        with open('src/json/matches.json', 'r') as json_file2:
            with open('src/json/matchesv2.json', 'r') as json_file3:
                with open('src/json/matchesv3.json', 'w') as json_file4:
                    matchSet = set()
                    for player in json.load(json_file)["entries"]:
                        matches_request = requests.get(url = PUUID_MATCHES_ENDPOINT +"/" + player["puuid"] +"/ids", params = {"api_key": API_KEY, "queue": 420, "type": "ranked", "count": 25})
                        if matches_request.status_code == 200:
                            #TODO
                            print("successful")
                            for i in matches_request.json():
                                matchSet.add(i)
                        else:
                            print("unsuccessful")
                        time.sleep(3)
            
                    matchSet = matchSet.difference(set(json.load(json_file2)["entries"])).difference(set(json.load(json_file3)["entries"]))
        
                    json.dump({"entries": list(matchSet)}, json_file4)


#SCHEMA PARSING
def schema_parser():
    with open('src/json/matchesv3.json', 'r') as json_file:
        with open('src/json/match_schemav3.json', 'w') as match_sql_schema:
            with open('src/json/player_match_schemav3.json', 'w') as player_sql_schema:
                match_schema = {"entries": []}; player_schema = {"entries": []}
                for i, match in enumerate(json.load(json_file)["entries"]):
                    match_request = requests.get(url = MATCHID_MATCHES_ENDPOINT + "/" + match, params = {'api_key': API_KEY})
                    print(i, match_request.status_code)
                    if match_request.status_code == 200:
                        jsonData = match_request.json()
                        match_data = {"gameDuration": jsonData["info"]["gameDuration"], "gameId": jsonData["info"]["gameId"],
                                "gameResult": 100 if jsonData["info"]["teams"][0]["win"] and jsonData["info"]["teams"][0]["teamId"] == 100 else 200}
                        for i in range(10):
                            match_data["participant" + str(i + 1)] = {"puuid": jsonData["metadata"]["participants"][i],"championId": jsonData["info"]["participants"][i]["championId"], "championName": jsonData["info"]["participants"][i]["championName"]}
                            participant_data = {"gameId": jsonData["info"]["gameId"], "puuid": match_data["participant" + str(i+1)]["puuid"],
                                    "championId": match_data["participant" + str(i+1)]["championId"], "championName": match_data["participant" + str(i+1)]["championName"],
                                    "teamId": "blue" if jsonData["info"]["participants"][i]["teamId"] == 100 else "red",
                                    "lane": jsonData["info"]["participants"][i]["lane"],
                                    "kills": jsonData["info"]["participants"][i]["kills"],
                                    "deaths": jsonData["info"]["participants"][i]["deaths"],
                                    "assists": jsonData["info"]["participants"][i]["assists"],
                                    "physicalDamageDone": jsonData["info"]["participants"][i]["physicalDamageDealtToChampions"],
                                    "magicDamageDone": jsonData["info"]["participants"][i]["magicDamageDealtToChampions"],
                                    "objectiveDamage": jsonData["info"]["participants"][i]["damageDealtToObjectives"]}
                            for j in range(7):
                                participant_data["item" + str(j)] = jsonData["info"]["participants"][i]["item" + str(j)]

                            match_schema["entries"].append(match_data); player_schema["entries"].append(participant_data)
                
                
                    else:
                        print("Failure to run this match due to Error", match_request.status_code)
                
                    time.sleep(2)

                json.dump(match_schema, match_sql_schema); json.dump(player_schema, player_sql_schema)

#SCHEMA DATA UPDATE WITH CHALLENGER DATA + 5 more matches per puuid
def schema_updating():
    with open('src/json/match_schemav3.json', 'r', encoding = "utf-8") as json_file1:
        with open('src/json/player_match_schemav3.json', 'r', encoding = "utf-8") as json_file2:

            match_prevVer = set([entry["gameId"] for entry in json.load(open('src/json/player_match_schema.json', 'r'))["entries"]])
        
            container_player_schema = defaultdict(list)
            container_match_schema = defaultdict(list)
            visited = set()

            for entry in json.load(json_file1)["entries"]:
                print(entry["gameId"])
                if entry["gameId"] not in match_prevVer and entry["gameId"] not in visited:
                    container_match_schema["entries"].append(entry)
                    visited.add(entry["gameId"])
            for entry in json.load(json_file2)["entries"]:
                if entry["gameId"] not in match_prevVer:
                    container_player_schema["entries"].append(entry)
                
            player_match_json = open('src/json/player_match_schema_master.json', 'w')
            match_json = open('src/json/match_schema_master.json', 'w')
            json.dump(container_player_schema, player_match_json)
            json.dump(container_match_schema, match_json)
            player_match_json.close()
            match_json.close()


#DATA TRANSFER TO CSV FILES
def match_schema_translation():
    with open('src/json/match_schema_master.json', 'r') as json_file:
        container_match = defaultdict(list)
        entries_match = json.load(json_file)["entries"]
        game_ids = set()
        breakpoint = 0
        for i, entry in enumerate(entries_match):
            if entry["gameId"] in game_ids:
                continue
            else:
                game_ids.add(entry["gameId"])
            for key, value in entry.items():
                if key.find('participant') != -1:
                    container_match[key].append(value["puuid"])
                else:
                    container_match[key].append(value)
            if i % 3000 == 2999:
                df = pandas.DataFrame(data = container_match)
                df.to_csv('src/csv/match_schema_master' + str(breakpoint) + ".csv", index = None)
                breakpoint += 1
                container_match.clear()
        df = pandas.DataFrame(data = container_match)
        df.to_csv('src/csv/match_schema_master' + str(breakpoint) + ".csv", index = None)


def player_match_translation():
    with open('src/json/player_match_schema_master.json', 'r') as json_file:
        container_player = defaultdict(list)
        entries_match = json.load(json_file)["entries"]
        breakpoint = 0
        for i, entry in enumerate(entries_match):
            for key, value in entry.items():
                container_player[key].append(value)
            if i % 3000 == 2999:
                df = pandas.DataFrame(data = container_player)
                df.to_csv('src/csv/player_match_master/player_match_schema_master' + str(breakpoint) + '.csv', index = None)
                container_player.clear()
                breakpoint += 1
        df = pandas.DataFrame(data = container_player)
        df.to_csv('src/csv/player_match_master/player_match_schema_master' + str(breakpoint) + '.csv', index = None)
        print("Finished")


#TRANSLATE ITEMS INTO CSV
def items_csv():
    with open('item.json', 'r') as json_file:
        container_items = defaultdict(list)
        item_data = json.load(json_file)
    
        for itemId, value in item_data["data"].items():
            container_items["itemId"].append(itemId)
            container_items["name"].append(value["name"])

        df = pandas.DataFrame(data = container_items)
        df.to_csv('items.csv', index = None)


#TRANSLATE CHAMPIONS INTO CSV
def champions_csv():
    with open('champion.json', encoding = "utf-8") as json_file:
        container_champions = defaultdict(list)
        champion_data = json.load(json_file)

        for champion, data in champion_data["data"].items():
            container_champions["name"].append(champion)
            container_champions["id"].append(data["key"])
            container_champions["role1"].append(data["tags"][0])
            if len(data["tags"]) ==2: container_champions["role2"].append(data["tags"][1])
            else: container_champions["role2"].append("N/A")
            for stat, value in data["info"].items():
                container_champions[stat].append(value)
        df = pandas.DataFrame(data = container_champions)
        df.to_csv('champions.csv', index = None)


#CREATE CSV FOR IGNORED ITEMS
def ignored_items():
    with open('./src/json/item.json', encoding = 'utf-8') as json_file:
        container_ignored_items = defaultdict(list)
        item_data = json.load(json_file)
        ignored_items = set([2055,0, 2003, 2031, 2033, 3330, 3340, 3363, 3364, 2138,2139, 2140, 3400, 1054, 1055, 1056, 1035, 1039, 1083, 2010, 2403])

        for item, data in item_data["data"].items():
            if int(item) in ignored_items:
                container_ignored_items["itemId"].append(item)
                container_ignored_items["itemName"].append(data["name"])
    
        df = pandas.DataFrame(data = container_ignored_items)
        df.to_csv('./src/csv/ignored_items.csv', index = None)


#CREATE CSV FOR CHAMPION VS CHAMPION WIN RATE
def champvschamp():
    #Challenger section
    with open('src/json/player_match_schema_challenger.json', 'r', encoding= "utf-8") as json_file1:
        with open('src/json/match_schema_challenger.json', 'r', encoding = "utf-8") as json_file2:
            with open('src/json/champion.json', 'r', encoding = "utf-8") as json_file3:
                challenger_players = json.load(json_file1)
                challenger_matches = json.load(json_file2)
                champions = json.load(json_file3)
                container_total_data = defaultdict(dict)
                champion_data = dict()

                #DATA STRUCTURE TO MAKE
                #CHAMPION| CHAMPION -> WINS, ITEMS PLAYED
                #First, collect all info into a list, then translate this to integers after calculations are finished
                for champion in champions["data"].keys():
                    for champion2 in champions["data"].keys():
                        if champion != champion2:
                            champion_data[champion.lower() + "|" + champion2.lower()] = defaultdict(Bag)

                

                for entry in challenger_players["entries"]:
                    container_total_data[entry["gameId"]][entry["puuid"]] = entry 
            
                for match in challenger_matches["entries"]:
                    matchResult = "blue" if match["gameResult"] == 100 else "red"
                    gameId = match["gameId"]
                    puuids = [puuid for puuid in container_total_data[gameId]]
                    #calculations for blue team
                    for i in range(0, 5):
                        for j in range(5,10):
                            champion_data[container_total_data[gameId][puuids[i]]["championName"].lower() + "|" + container_total_data[gameId][puuids[j]]["championName"].lower()]["winRate"].add(1 if matchResult == "blue" else 0)
                            for item_num in range(0, 7):
                                champion_data[container_total_data[gameId][puuids[i]]["championName"].lower() + "|" + container_total_data[gameId][puuids[j]]["championName"].lower()]["items"].add(container_total_data[gameId][puuids[i]]["item" + str(item_num)])

                    #calculations for red team
                    for i in range(5, 10):
                        for j in range(0,5):
                            champion_data[container_total_data[gameId][puuids[i]]["championName"].lower() + "|" + container_total_data[gameId][puuids[j]]["championName"].lower()]["winRate"].add(1 if matchResult == "red" else 0)
                            for item_num in range(0, 7):
                                champion_data[container_total_data[gameId][puuids[i]]["championName"].lower() + "|" + container_total_data[gameId][puuids[j]]["championName"].lower()]["items"].add(container_total_data[gameId][puuids[i]]["item" + str(item_num)])

                #Calculating the rates for each bag
                for matchup in champion_data.keys():
                    champion_data[matchup]["winRate"].sum(); champion_data[matchup]["winRate"].updateItemStats()
                    champion_data[matchup]["items"].sum(); champion_data[matchup]["items"].updateItemStats()

                #TRANSLATE INTO A DATA STRUCTURE SUITABLE FOR JSON -> CSV
                translationItems = dict()
                translationWinRate = defaultdict(list)

                #Holds the ordering of the items.
                itemHashMap = dict()

                with open('src/json/item.json','r', encoding = "utf-8") as json_file4:
                    items = json.load(json_file4)
                    totalItems = len(items["data"])
                    
                    #Sets the hashmap for the items
                    for i, item in enumerate(items["data"].keys()):
                        itemHashMap[item] = i
                    

                    for matchup in champion_data.keys():
                        #Setups for Items and does Matchup Data at same time
                        translationItems[matchup] = [0 for i in range(totalItems)]
                        translationWinRate["matchup"].append(matchup)
                        translationWinRate["winRate"].append(champion_data[matchup]["winRate"].getStats()[1])
                        translationWinRate["totalMatches"].append(champion_data[matchup]["winRate"].total)

                        for item, pickRate in champion_data[matchup]["items"].getStats().items():
                            if str(item) != '0':
                                translationItems[matchup][itemHashMap[str(item)]] = pickRate

                    items2D = np.array([itemList for itemList in translationItems.values()])

                    for key,value in itemHashMap.items():
                        translationWinRate[items["data"][key]["name"]] = items2D[:,value]
                    
                    df = pandas.DataFrame(data = translationWinRate)
                    df.to_csv('src/csv/itemMatchup.csv', index = None)
            
if __name__ == "__main__":
    champvschamp()