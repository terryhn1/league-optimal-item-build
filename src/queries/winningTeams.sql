with redPlayers(gameId, puuid, championName, teamId, lane, kills, deaths, assists, physicalDamageDone, magicDamageDone, item0, item1, item2, item3, item4, item5, item6) as
	(SELECT matches.gameId, player_result.puuid, player_result.championName, player_result.teamId, player_result.lane, player_result.kills, player_result.deaths, player_result.assists, player_result.physicalDamageDone, player_result.magicDamageDone, player_result.item0, player_result.item1, player_result.item2, player_result.item3,player_result.item4, player_result.item5, player_result.item6
	FROM matches, player_result
	WHERE matches.gameDuration >1800000 and matches.gameId = player_result.gameId and matches.gameResult = 200 and player_result.teamId = "red" and (player_result.physicalDamageDone > 10000 or player_result.magicDamageDone > 10000)
    ),
    bluePlayers(gameId, puuId, championName, teamId, lane, kills, deaths, assists, physicalDamageDone, magicDamageDone, item0, item1, item2, item3, item4, item5, item6) as
    (SELECT matches.gameId,player_result.puuid, player_result.championName, player_result.teamId, player_result.lane, player_result.kills,player_result.deaths, player_result.assists, player_result.physicalDamageDone, player_result.magicDamagedone, player_result.item0, player_result.item1, player_result.item2, player_result.item3, player_result.item4, player_result.item5, player_result.item6
    FROM matches, player_result
    WHERE matches.gameDuration > 1800000 and matches.gameId = player_result.gameId and matches.gameResult = 100 and player_result.teamId = "blue" and (player_result.physicalDamageDone > 10000 or player_result.magicDamageDone > 10000)
    )
    
select championName
from bluePlayers
where (kills + assists)/(deaths +1) > 7;