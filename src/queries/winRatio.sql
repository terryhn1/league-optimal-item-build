with redWins(championName, count) as
	(select player_result.championName, count(player_result.championName)
	from player_result, matches
	where matches.gameId = player_result.gameId and matches.gameResult = 200 and player_result.teamId = "red"
    group by player_result.championName
    ),
    blueWins(championName, count) as
    (select player_result.championName, count(championName)
    from player_result, matches
    where matches.gameId = player_result.gameId and matches.gameResult = 100 and player_result.teamId = "blue"
    group by player_result.championName
    ),
    totalGames(championName, count) as
    (select championName, count(championName)
    from player_result
    group by championName)

select blueWins.championName, (blueWins.count + redWins.count) as totalWins, totalGames.count as totalGamesPlayed, (blueWins.count + redWins.count)/totalGames.count as winRatio
from blueWins, redWins, totalGames
where blueWins.championName = redWins.championName and totalGames.championName = redWins.championName
order by winRatio DESC;