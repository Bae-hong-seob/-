-- 코드를 입력하세요
SELECT NAME, count(*) AS COUNT
FROM ANIMAL_INS
WHERE name is not NULL
GROUP BY NAME
HAVING count(*) >= 2
ORDER BY NAME