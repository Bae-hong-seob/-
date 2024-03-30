-- 코드를 입력하세요
SELECT P.product_code, SUM(P.price*O.sales_amount)
FROM product AS P
JOIN offline_sale AS O ON P.product_id = O.product_id
GROUP BY P.product_code
ORDER BY SUM(P.price*O.sales_amount) DESC, P.product_code