# Level 1
- Bruce Force 주로 출제.(=구현 문제) 일단 풀고 볼 것
- 낮은 수준에서 구현은 수학적인 사고가 진짜 중요함. 엄청 간결해질 수 있음.

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

4. 제곱, 제곱근 함수 - n**2, n**(1/2) or import math - pow(), sqrt() 함수
- pow(n,2) : return n**2 
- sqrt(n) : return n 제곱근
- 둘다 return float type

~~~
sqrt_n = n**(1/2)
n = n**2
~~~
~~~
import math

sqrt_n = math.sqrt(n)
n = math.pow(sqrt_n,2)
~~~

5. 리스트 -> 문자열 변환 = ''.join(list)함수 사용
~~~
def solution(n):
    n = [i for i in str(n)]
    n.sort(reverse=True)
    return int("".join(n))
~~~

6. .index('what') 함수
~~~
def solution(seoul):
    return '김서방은 '+str(seoul.index('Kim'))+'에 있다'
~~~

7. list, string 정렬 : .sort(reverse=True or False) 사용 | sorted(list or string, reverse=True or False) 사용.
- .sort() 함수는 return 값이 없음.
- sorted(list)는 list를 정렬하여 return

8. 반복문 zip(list, list)함수 잘 쓰기
~~~
for absolute, sign in zip(absolutes, signs):
  print(absolute, sign)
~~~

9. try-except 문
- 오류 발생 시 바로 except 문 내용 실행.
~~~
# 정수로만 이루어진 문자열인지 확인
def solution(s):
    if len(s)==4 or len(s)==6:
        try:
            s = int(s)
            return True
        except:
            return False
    else:
        return False
~~~

10. int()함수
- int(value, 진법)
- int(10,3) -> 101 변환 가능
~~~
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
~~~

## 직관적인 for 문 사용 (if 문만 = for문 뒤에, if-else문 = for문 앞에)
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

~~~
# if-else 사용할 경우 for 문 앞에 적어야함.
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
~~~

~~~
#연산식도 가능
def solution(x, n):
    return [x+x*i for i in range(n)]
~~~

## 직관적인 return문 사용
~~~
return num_p == num_y
~~~

~~~
#or 문도 적용 가능
return sorted([n for n in arr if n%divisor == 0]) or [-1]
~~~

## 리스트, 문자열 모두 for문 하나씩 접근 가능
~~~
x = ['1', '2', '3']
int(c) for c in x
~~~

~~~
x = 123
int(c) for c in str(x)
~~~
