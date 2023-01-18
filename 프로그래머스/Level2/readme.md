# 자주 사용하는 함수 정리

1. list 내 string -> int 등 type 변환 **list(map()) 사용**
~~~
    num_list = list(map(int, num_list))
~~~
2. String 내장함수 upper(), lower(), replace('what', 'how')
~~~
string.upper()
string.lower()
output = string.replace('what','how') #string은 변함없이 바꾼값을 return한다는 점을 유의
~~~
- String : replace 모두바꿈, List : remove 맨 앞에 하나만 삭제


3. list() : 문자열 문자 하나하나 -> 리스트의 원소 하나하나로 변환
~~~
str = "python"
my_list = list(str)

print(my_list)
>['p', 'y', 't', 'h', 'o', 'n']
~~~
    
4. split()
- split( )은 공백이 1개이건 2개이건 n개이건 상관없이 무조건 1개로 보고 처리  
- split(" ")은 공백 1개, 1개를 각각의 공백으로 따로따로 처리합니다. 
- 추가적으로 split( )은 공백만 처리하는 것이 아니라 "\t" ( 탭 ), "\n" ( 엔터 ) 도 처리해줍니다.
~~~
string = "word1 word2  word3    word4     "
#word1 뒤에 공백 1개, word2 뒤에 공백 2개, word3 뒤에 공백 3개, word4 뒤에 공백 4개

print(string.split())
> ['word1', 'word2', 'word3', 'word4']
print(string.split(" "))
> ['word1', 'word2', '', 'word3', '', '', 'word4', '', '', '', '']
~~~

5. join()
- ''.join(리스트) , '구분자'.join(리스트)
- ''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수인 것입니다.
- '구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.
- '_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.
~~~
answer = ''.join(string)
~~~

6. zip()
- zip() 함수는 **여러 개의** 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
~~~
>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for pair in zip(numbers, letters):
...     print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')
~~~

7. 구조(stack, queue, deque) -> 모두 deque를 불러와서 사용함
~~~
from collections import deque

dq=deque() # 덱 생성
dq.append() # 덱의 가장 오른쪽에 원소 삽입
dq.popleft() # 가장 왼쪽 원소 반환
dq.appendleft() # 덱의 가장 왼쪽에 원소 삽입
dp.pop() # 가장 오른쪽 원소 반환
dp.clear() # 모든 원소 제거
dp.copy() # 덱 복사
dp.count(x) #x와 같은 원소의 개수를 계산
~~~

8. format(num, 'type') -> format(n, 'b) 2진수, 8진수, 16진수 변환 함수
~~~
b = format(value, 'b') #2진수
o = format(value, 'o') #8진수
h = format(value, 'x') #16진수
~~~

9. 최대공약수
~~~
from fractions import gcd

answer = gcd(a,b) #a와b의 최대공약수 return
~~~

10. 최소공배수 : a*b / gcd(a,b)
~~~
from fractions import gcd

answer = a*b / gcd(a,b)
~~~

11. math.factorial(n) 팩토리얼 계산
~~~
import math

n = 10
answer = math.factorial(n)
~~~

# 문제 유형 정리

1. A리스트와 B리스트의 인자들을 곱하고 더한 값의 최솟값을 찾는 문제
- A리스트의 최솟값과 B리스트의 최댓값을 곱하면서 진행하는것이 가장 효율적으로 최솟값을 찾는 방법
- 따라서 A리스트는 오름차순으로 정렬하고, B리스트는 내림차순으로 정렬하여 순차적으로 곱하여 더한값을 리턴

2. 괄호,알파벳 등 "짝지어졌는지" -> deque(=스택)을 활용하는 대표적인 문제 유형
- list에서 pop 진행하는거랑 deque에서 pop 진행하는거랑 시간차이남. 되도록이면 deque구조를 사용할 것.
- s에서 for문을 돌며, 여는 괄호 : '(' 가 나오면 stack에 element를 추가하고, 닫는 괄호 : ')' 가 나오면 stack에서 element를 뺌.
- <mark> 다 끝나고 len(dq)==0 인지 검사할 것 ex) '(((' </mark>  
<span style="color:red">다 끝나고 len(dq)==0 인지 검사할 것 ex) '(((' </span>
- 비슷한 문제로는 백준의 쇠막대기 문제가 있습니다.

3. 알고리즘이 잘 떠오르지 않을 때 : 전역탐색(Brute Force) 

4. 피보나치 수 : 반복문, 재귀함수
- 반복문 : 리스트 활용(값을 저장해놓는게 다시 계산안해도 되서 빠르다)
- 재귀함수 : 직관적이지만 느리다

5. 최대공약수, 최소공배수 : 유클리디안 호제법 gcd 사용하면 쉽게 얻을 수 있다.
- 유클리드 호제법이란 숫자 a, b가 있을 때, a를 b로 나눈 나머지와 b의 최대 공약수 = a와b 의 최대 공약수와 같다는 것을 의미한다.
- 그럼, 계속해서 a 를 b로 나누어서 - a=b, b=a%b에 대입시켜서 b 가 0이 될때 까지 반복하면, 남는 a 값이 바로 최대 공약수 이다.
~~~
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
~~~
- 최소공배수는 a, b의 곱을 a, b의 최대 공약수로 나누면 나오게 된다.
~~~
def lcm(a, b):
    return a * b / gcd(a, b)
~~~

# 주요 개념
1. 시간복잡도 고려해서 짜기
- 다중 반복문은 사용 주의
- if문 또한 시간복잡도 계산 시 상수처리 되지만, 남발은 좋지않음. 대입이 훨씬 빠름

# 스스로 못 푼 문제
1. <s>점프와 순간이동</s> solve
2. 멀리 뛰기 : 팩토리얼 문제 완전탐색으로 풀어서 시간초과 뜸
3. H-index : h-index 생각을 잘못했음.  
    다음과 같은 테스트 케이스를 생각해보자 citations = [6,6,6,6,6,1] 일 때  이 과학자의 H-Index는?
    - 이 상황에서 답은 5이다. 위 예시를 든 이유는 일부 사람들이 h값을 citations 리스트 안에 있는 값 중에서 고르려고 하기 때문이다.
    - 이런 케이스까지 성공적으로 해결하는 코드를 작성하기 위해서 우리는 H-index의 최댓값과 citations 리스트의 길이의 관계를 고려하면서 문제를 풀어나가야 한다.
4. 행렬의 곱셈 : 3중 for문
