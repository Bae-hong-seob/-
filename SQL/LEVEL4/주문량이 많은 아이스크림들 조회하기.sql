-- 코드를 입력하세요
SELECT J.flavor
FROM july AS J
LEFT OUTER JOIN first_half AS F ON J.shipment_id=F.shipment_id
GROUP BY J.flavor
ORDER BY SUM(J.total_order)+F.total_order DESC
LIMIT 3