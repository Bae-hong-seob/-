# 기본 공식(암기 필수)
~~~
SELECT column1,column2,etc... # '*' 는 모든 열을 의미.
DISTINCT table1.column1 #column1은 중복된 값 제거.
FROM table1
JOIN table1 ON table1.column2 = table2.column5
WEHRE column1>10 and column2>2
GROUP BY
HAVING
ORDER BY column1 DESC, column2
LIMIT 3 #결과값 상위 3개만 출력
OFFSET
~~~



사용할 수 있는 내장 라이브러리 : SUM(), AVG(), ROUND(value,0)  


결측치 대체
~~~
COALESCE(TLNO, 'NONE') AS TLNO
~~~
