with championGameCount(championName, gamesPlayed) as (
	select championName, count(championName) as count
	from player_result
	group by championName
	order by count DESC
)

select *
from championGameCount;