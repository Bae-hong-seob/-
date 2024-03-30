-- 코드를 입력하세요
SELECT B.book_id, A.author_name, DATE_FORMAT(B.published_date, '%Y-%m-%d')
FROM book AS B
JOIN author AS A ON B.author_id=A.author_id
WHERE category='경제'
ORDER BY B.published_date