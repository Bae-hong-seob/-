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

# 내장 함수
- table.column is NULL 로 해야한다. table.column = NULL 이거 안먹음.
- DATETIME 관련하여 YEAR(), MONTH(), DAY() 함수 기억
- COUNT() 함수
- 변수명 변경: AS -> COUNT(table.column) AS 개수
- LIKE 연산자. 조건문에 쓰임 -> '%탐색문자%' C언어 배울때 배우던거
  ~~~
  SELECT animal_id, name
  FROM animal_ins
  WHERE name LIKE '%el%' AND animal_type = 'Dog'
  ORDER BY name
  ~~~
- COALESCE(column1, 'N') -> column1의 결측치를 'N'으로 대체. 발음 코 얼레스. CO AL ESCE
- DATE_FORMAT(column1, '%Y-%m-%d) -> datetime을 어떻게 표현할 것인가에 대해
  ~~~
  예시로 2024-03-01 23:05:01이 있다고 하자.
  %Y : 2024, %y : 24
  %M : March, %m : 03, %c : 3
  %D : 1st, %d : 1
  %H : 23, %h : 11
  %i : 05 # m이 month랑 minute 둘다 의미하기 때문에 필수로 외워야함. m은 month, i는 m'i'nute
  %s : 01
  ~~~
- SELECT IF(column > 3, 'Y', 'N') -> if(조건문, 참일 때 반환 값, 거짓일 때 반환 값)
  - IF(column <=3, 'LOW', IF(column<=10, 'MEDIUM", "HIGH)) 이렇게 쓸 수도 있음. 3이하일 때는 'LOW', 3초과 10이하일 때는 "MEDIUM", 10초과일 때는 'HIGH"
- CONCAT()함수. -> CONCAT(MAX(length), 'cm')
  - CONCAT(MAX(length),'verse' ,'cm') 이렇게 3개를 넣어도 됨
- ROUND()함수 -> ROUND(value, 0) value를 0자릿수에서 반올림
  - 올림: CEIL(N)
  - 내림: FLOOR(N)
  - 버림: TRUNC(N, 0)
- SUBSTR(string, start_index, end_index) : 이때 파이썬과 달리 index 1부터 시작한다
