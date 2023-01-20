# Level 1
- Bruce Force 주로 출제.(=구현 문제) 일단 풀고 볼 것

# 기본 개념 - 내장함수, 가독성 높은 표현
1. enumerate() 함수. list에서 index와 value를 모두 가져와야할 때 사용
~~~
for idx, value in enumerate(list):
  print(idx, value)
~~~

2. reversed() 함수. 단 return은 메모리주소. 하나씩 접근하여 값을 추출해야함.
~~~
#n=12345, 역순으로 출력하기
def solution(n):
    return list(int(i) for i in reversed(str(n)))
~~~

3. map() 함수. map(function, list)
- list 각 원소에 function을 적용하여 return.
- 단, return이 map type이므로 내가 원하는 자료형으로 변환 필요
~~~
#n=12345, n의 역순출력
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
~~~

4. 직관적인 for 문 사용 (if 문도 가능)
~~~
#n=123, 각 자릿수 더하기
def solution(n):    
    return sum([int(i) for i in str(n)])
~~~

~~~
#n=12, 약수 모두 더하기
def solution(n):
    return n+sum([i for i in range(1,n//2+1) if n%i ==0])
~~~
