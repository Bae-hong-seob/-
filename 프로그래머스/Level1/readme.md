# Level 1
- Bruce Force 주로 출제.(=구현 문제) 일단 풀고 볼 것

# 기본 개념
1. enumerate() 함수. list에서 index와 value를 모두 가져와야할 때 사용
~~~
for idx, value in enumerate(list):
  print(idx, value)
~~~

2. 직관적인 for 문 사용
~~~
#n=123, 각 자릿수 더하기
def solution(n):    
    return sum([int(i) for i in str(n)])
~~~
