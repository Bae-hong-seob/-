# 기본 공식(암기 필수)
~~~
SELECT column1,column2,etc... # '*' 는 모든 열을 의미.
DISTINCT table1.column1 #column1은 중복된 값 제거.
FROM table1
JOIN table1 ON table1.column2 = table2.column5 #기본적으로 INNER 조인을 의미함. LEFT OUTER JOIN / RIGHT OUTER JOIN 을 사용하는 경우도 존재
WEHRE column1>10 and column2>2
GROUP BY
HAVING
ORDER BY column1 DESC, column2
LIMIT 3 #결과값 상위 3개만 출력
OFFSET
~~~

- 그룹화 한 다음엔 일반 컬럼은 SELECT 할 수 없다. GROUP BY 절에 명시된 컬럼만 SELECT 된다. 이외에는 집계함수가 와야함.
  - 집계함수 종류: SUM(), MAX(), MIN(), COUNT(), AVG, STDEV(), VAR()
  - 따라서 이외의 SELECT 문에 column명을 적어야한다면 GROUP BY가 아니라 WHERE (column1, column2) IN (SELECT FROM WEHRE ~) 식의 서브쿼리 방법을 이용해야한다.

# 서브쿼리 활용 잘하기.
~~~
-- 코드를 작성해주세요
SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX_SIZE-size_of_colony AS YEAR_DEV, ID
FROM ecoli_data AS A
JOIN (
    SELECT YEAR(DIFFERENTIATION_DATE) AS BORN_YEAR, MAX(size_of_colony) AS MAX_SIZE
    FROM ecoli_data
    GROUP BY YEAR(DIFFERENTIATION_DATE)
) AS B ON YEAR(A.DIFFERENTIATION_DATE) = B.BORN_YEAR
ORDER BY YEAR, YEAR_DEV
~~~


결측치 대체
~~~
COALESCE(TLNO, 'NONE') AS TLNO
~~~
