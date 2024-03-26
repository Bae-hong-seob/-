-- 코드를 입력하세요
SELECT LEFT(product_code,2) AS CATEGORY, count(*) AS PRODUCTS
FROM product
GROUP BY LEFT(product_code,2)