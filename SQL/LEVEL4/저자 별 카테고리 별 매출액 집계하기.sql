-- 코드를 입력하세요
SELECT author_id, author_name, category, SUM(sales*price) AS TOTAL_SALES
FROM book_sales AS S
JOIN (
    SELECT B.book_id, B.category, B.author_id,B.price,B.published_date, A.author_name
    FROM book AS B
    JOIN author AS A ON B.author_id = A.author_id
) AS C ON S.book_id = C.book_id
WHERE YEAR(S.sales_date)=2022 and MONTH(S.sales_date)=1
GROUP BY author_id, author_name, category
ORDER BY author_id, category DESC