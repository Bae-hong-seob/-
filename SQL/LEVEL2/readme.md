MAX(), MIN() 함수는 해당 column에서만 작동. 즉 다른 column의 값들은 MAX(column1)에 해당하는 row의 값들을 반환하지 않는다.

~~~
GROUP BY mcdp_cd
ORDER BY count(*), mcdp_cd # 그룹별 count가 작동한다.
~~~
