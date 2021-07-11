select *
from itemwinrate
where totalMatches != 0 and totalMatches > 30 and winRate > 0.5
order by matchUp, winRate DESC;