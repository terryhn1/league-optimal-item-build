with item0Col(championName, itemId, itemName, count) as
	(select player_result.championName, player_result.item0, items.name, count(items.name) as count from player_result, items where player_result.item0 = items.itemId group by player_result.championName, items.itemId),
    item1Col(championName, itemId, itemName, count) as
    (select player_result.championName, player_result.item1, items.name, count(items.name) as count from player_result, items where player_result.item1 = items.itemId group by player_result.championName, items.itemId),
    item2Col(championName, itemId, itemName, count) as
    (select player_result.championName, player_result.item2, items.name, count(items.name) as count from player_result, items where player_result.item2 = items.itemId group by player_result.championName, items.itemId),
    item3Col(championName, itemId, itemName, count) as
    (select player_result.championName, player_result.item3, items.name, count(items.name) as count from player_result, items where player_result.item3 = items.itemId group by player_result.championName, items.itemId),
    item4Col(championName, itemId, itemName, count) as
    (select player_result.championName,player_result.item4, items.name, count(items.name) as count from player_result, items where player_result.item4 = items.itemId group by player_result.championName, items.itemId),
    item5Col(championName, itemId, itemName, count) as
    (select player_result.championName, player_result.item5, items.name, count(items.name) as count from player_result, items where player_result.item5 = items.itemId group by player_result.championName, items.itemId),
    item6Col(championName, itemId, itemName, count) as
    (select player_result.championName, player_result.item6, items.name, count(items.name) as count from player_result, items where player_result.item6 = items.itemId group by player_result.championName, items.itemId),
    
    combined(championName, itemId, itemName, count) as
	(select * from item0Col UNION ALL select * from item1Col UNION ALL select * from item2Col UNION ALL select * from item3Col UNION ALL select * from item4Col UNION ALL select * from item5Col UNION ALL 
	select * from item6Col order by championName, itemId),
    
    totalItemUsage(championName, itemId, itemName, count) as
    (select championName, itemId, itemName, sum(count) as total
	from combined
	group by championName, itemId, itemName
	order by championName, total DESC),
    
    teamConversion(gameId, gameResult) as
    (select gameId, IF(gameResult = 100, "blue", "red") from matches),
    
    item0Win(championName, itemId, itemName, count) as
	(select player_result.championName, player_result.item0, items.name, count(items.name) as count from player_result, items,teamConversion where player_result.item0 = items.itemId and teamConversion.gameId = player_result.gameId and player_result.teamId = teamConversion.gameResult group by player_result.championName, items.itemId),
    item1Win(championName, itemId, itemName, count) as
    (select player_result.championName, player_result.item1, items.name, count(items.name) as count from player_result, items, teamConversion where player_result.item1 = items.itemId and teamConversion.gameId = player_result.gameId and player_result.teamId = teamConversion.gameResult group by player_result.championName, items.itemId),
    item2Win(championName, itemId, itemName, count) as
    (select player_result.championName, player_result.item2, items.name, count(items.name) as count from player_result, items, teamConversion where player_result.item2 = items.itemId and teamConversion.gameId = player_result.gameId and player_result.teamId = teamConversion.gameResult group by player_result.championName, items.itemId),
    item3Win(championName, itemId, itemName, count) as
    (select player_result.championName, player_result.item3, items.name, count(items.name) as count from player_result, items, teamConversion where player_result.item3 = items.itemId and teamConversion.gameId = player_result.gameId and player_result.teamId = teamConversion.gameResult group by player_result.championName, items.itemId),
    item4Win(championName, itemId, itemName, count) as
    (select player_result.championName,player_result.item4, items.name, count(items.name) as count from player_result, items, teamConversion where player_result.item4 = items.itemId and teamConversion.gameId = player_result.gameId and player_result.teamId = teamConversion.gameResult group by player_result.championName, items.itemId),
    item5Win(championName, itemId, itemName, count) as
    (select player_result.championName, player_result.item5, items.name, count(items.name) as count from player_result, items, teamConversion where player_result.item5 = items.itemId and teamConversion.gameId = player_result.gameId and player_result.teamId = teamConversion.gameResult group by player_result.championName, items.itemId),
    item6Win(championName, itemId, itemName, count) as
    (select player_result.championName, player_result.item6, items.name, count(items.name) as count from player_result, items, teamConversion where player_result.item6 = items.itemId and teamConversion.gameId = player_result.gameId and player_result.teamId = teamConversion.gameResult group by player_result.championName, items.itemId),
    
	combined2(championName, itemId, itemName, count) as
	(select * from item0Win UNION ALL select * from item1Win UNION ALL select * from item2Win UNION ALL select * from item3Win UNION ALL select * from item4Win UNION ALL select * from item5Win UNION ALL 
	select * from item6Win order by championName, itemId),


    totalWinItemUsage(championName, itemId, itemName, winCount) as
	(select championName, itemId, itemName, sum(count) as total
	from combined2
	group by championName, itemId, itemName
	order by championName, total DESC)


select totalItemUsage.championName,totalItemUsage.itemId, totalItemUsage.itemName, totalWinItemUsage.winCount, totalItemUsage.count as totalCount, totalWinItemUsage.winCount/ totalItemUsage.count as winRatio
from totalWinItemUsage, totalItemUsage
where totalWinItemUsage.championName = totalItemUsage.championName and totalWinItemUsage.itemId = totalItemUsage.itemId and totalWinItemUsage.itemName = totalItemUsage.itemName and totalItemUsage.itemId not in (select itemId from ignored_items)
order by totalWinItemUsage.championName, winRatio DESC;