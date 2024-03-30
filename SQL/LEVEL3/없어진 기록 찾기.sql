-- 코드를 입력하세요
SELECT O.animal_id, O.name
FROM animal_ins AS I
RIGHT OUTER JOIN animal_outs AS O ON I.animal_id=O.animal_id
WHERE I.animal_id is NULL and O.animal_id is not NULL
ORDER BY animal_id