select distinct(type1), SUM(avg_speed), AVG(traveled_d), count(type1)
from mysql.objects
GROUP BY type1