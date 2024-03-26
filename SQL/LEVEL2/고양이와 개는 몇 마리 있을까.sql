-- 코드를 입력하세요
SELECT animal_type, count(*)
FROM animal_ins
WHERE animal_type = 'Dog' or animal_type = 'Cat'
GROUP BY animal_type
ORDER BY animal_type