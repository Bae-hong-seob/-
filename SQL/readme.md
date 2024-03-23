# 기본 공식(암기 필수)
~~~
SELECT column1,column2,etc...
DISTINCT
FROM table1
JOIN table1, table2 ON
WEHRE column1>10 and column2>2
GROUP BY
HAVING
ORDER BY column1 DECS, column2
LIMIT
OFFSET
~~~



사용할 수 있는 내장 라이브러리 : SUM(), AVG(), ROUND(value,0)  

칼럼 명 수정
~~~
SELECT column1 as change_name FROM table_name
~~~

결측치 대체
~~~
COALESCE(TLNO, 'NONE') AS TLNO
~~~
