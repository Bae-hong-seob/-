-- 코드를 입력하세요
SELECT animal_id, name, IF(sex_upon_intake LIKE '%Neutered%' or sex_upon_intake LIKE '%Spayed%', 'O','X') AS 중성화
FROM animal_ins
ORDER BY animal_id