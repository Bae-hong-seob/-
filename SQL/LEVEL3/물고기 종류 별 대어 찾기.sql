-- 코드를 작성해주세요
SELECT I.id AS ID, N.fish_name AS FISH_NAME, I.length AS LENGTH
FROM fish_info AS I 
JOIN fish_name_info AS N ON I.fish_type = N.fish_type
WHERE (I.fish_type,I.length) IN (
    SELECT fish_type, MAX(length)
    FROM fish_info
    GROUP BY fish_type
)
ORDER BY I.id