-- 코드를 입력하세요
SELECT I.ingredient_type, SUM(total_order) AS TOTAL_ORDER
FROM first_half AS F
JOIN icecream_info AS I ON F.flavor=I.flavor
GROUP BY I.ingredient_type