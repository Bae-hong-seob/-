-- 코드를 입력하세요
SELECT category, price, product_name
FROM food_product
WHERE category IN ('과자','국','김치','식용유') AND (category,price) IN (
    SELECT B.category, MAX(B.price)
    FROM food_product AS B
    GROUP BY B.category
)
ORDER BY price DESC