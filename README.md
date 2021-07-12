# league-optimal-item-build

League of Legends OIB is an application that looks through high ELO games in the thousands and uses the statistical data as support for giving your champion the best build possible.
Currently, League of Legends OIB is updated to only include general builds, and will include situational item build generators using machine learning technology.

# Repository Navigation 

Inside src:
-The scripts folder written contain python files that help calculate the math from the data and each script has a suited purpose(translating json files to csv files, algorithm to deep search for best build, etc).
-The json folder contains information from League of Legends Data Dragon and json files made from further data analysis based from the data given from Riot Games API.
-The csv folder contains information to feed into the mySQL database, which has been translated from json to csv.
-The queries folder contains information to find good criteria from getting responses back from mySQL.
