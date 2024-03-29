-- 코드를 입력하세요
SELECT category, SUM(sales) AS TOTAL_SALES
FROM book AS B
JOIN book_sales AS S ON B.book_id=S.book_id
WHERE S.sales_date LIKE '2022-01%'
GROUP BY B.category
ORDER BY category