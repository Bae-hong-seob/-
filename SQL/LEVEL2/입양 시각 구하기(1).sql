SELECT HOUR(datetime) AS HOUR, COUNT(*) AS COUNT
FROM animal_outs
WHERE HOUR(datetime)>=9 and HOUR(datetime) < 20
GROUP BY HOUR(datetime)
ORDER BY HOUR(datetime)