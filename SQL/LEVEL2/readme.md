MAX(), MIN() 함수는 해당 column에서만 작동. 즉 다른 column의 값들은 MAX(column1)에 해당하는 row의 값들을 반환하지 않는다.

~~~
GROUP BY mcdp_cd
ORDER BY count(*), mcdp_cd # 그룹별 count가 작동한다.
~~~

GROUP BY 시 특정 칼럼을 기준으로 묶게 되는데, SELECT *과 함께 사용하면 ERROR 가능성이 높다.
- 묶음 기준 칼럼 외에 나머지 칼럼들은 어떻게 처리해야할 지 모르기 때문에 묶음 칼럼 + SUM() or COUNT() 등 집계 함수로써 칼럼명을 재 정의해줘야한다.
