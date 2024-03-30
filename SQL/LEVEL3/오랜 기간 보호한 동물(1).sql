-- 코드를 입력하세요
SELECT I.name, I.datetime
FROM animal_ins AS I
LEFT OUTER JOIN animal_outs AS O ON I.animal_id=O.animal_id
WHERE O.animal_id is NULL
ORDER BY I.datetime
LIMIT 3