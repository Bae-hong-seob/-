GROUP BY 절에 선언된 column만 SELECT 에 적을 수 있다. 이외에는 집계함수가 와야함.
- 따라서 이외의 SELECT 문에 column명을 적어야한다면 GROUP BY가 아니라 WHERE (column1, column2) IN (SELECT FROM WEHRE ~) 식의 서브쿼리 방법을 이용해야한다. 
