-- 코드를 입력하세요
SELECT B.writer_id AS USER_ID, U.nickname AS NICKNAME, SUM(B.price) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS B
JOIN USED_GOODS_USER AS U ON B.writer_id = U.user_id
WHERE B.status = 'DONE'
GROUP BY B.writer_id, U.nickname
HAVING SUM(B.price) >= 700000
ORDER BY TOTAL_SALES