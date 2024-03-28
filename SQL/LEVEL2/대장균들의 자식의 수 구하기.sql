-- 코드를 작성해주세요
SELECT P.id, COUNT(C.parent_id) AS CHILD_COUNT
FROM ecoli_data AS P
LEFT OUTER JOIN ecoli_data AS C ON P.id = C.parent_ID
GROUP BY P.id
ORDER BY P.id