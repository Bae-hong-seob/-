-- 코드를 입력하세요
SELECT MONTH(start_date), car_id, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE car_id IN (
    SELECT car_id
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE YEAR(start_date)=2022 and MONTH(start_date) BETWEEN 8 AND 10
    GROUP BY car_id
    HAVING COUNT(*)>=5
) AND YEAR(start_date)=2022 and MONTH(start_date) BETWEEN 8 AND 10
GROUP BY MONTH(start_date), car_id
ORDER BY MONTH(start_date), car_id DESC