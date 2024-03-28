-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT
FROM fish_info AS I 
JOIN fish_name_info AS N ON I.fish_type=N.fish_type
WHERE N.fish_name = 'BASS' or N.fish_name='SNAPPER'
