-- 코드를 입력하세요
SELECT YEAR(sales_date), MONTH(sales_date), gender, COUNT(DISTINCT(I.user_id)) AS USERS
FROM user_info AS I
JOIN online_sale AS O on I.user_id=O.user_id
WHERE gender is not NULL
GROUP BY YEAR(sales_date), MONTH(sales_date), gender
ORDER BY YEAR(sales_date), MONTH(sales_date), gender