-- 코드를 입력하세요
SELECT B.title, B.board_id, R.reply_id, R.writer_id, R.contents, DATE_FORMAT(R.created_date, '%Y-%m-%d') AS created_date
FROM used_goods_board AS B, used_goods_reply AS R
WHERE B.board_id = R.board_id and YEAR(B.created_date)=2022 and MONTH(B.created_date)=10 
ORDER BY R.created_date, B.title