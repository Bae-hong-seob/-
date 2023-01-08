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

# 문제 유형 정리

1. A리스트와 B리스트의 인자들을 곱하고 더한 값의 최솟값을 찾는 문제
- A리스트의 최솟값과 B리스트의 최댓값을 곱하면서 진행하는것이 가장 효율적으로 최솟값을 찾는 방법
- 따라서 A리스트는 오름차순으로 정렬하고, B리스트는 내림차순으로 정렬하여 순차적으로 곱하여 더한값을 리턴

2. 괄호가 바르게 짝지어졌는지 판단하는 문제는 스택을 활용하는 대표적인 문제 유형
- s에서 for문을 돌며, 여는 괄호 : '(' 가 나오면 stack에 element를 추가하고, 닫는 괄호 : ')' 가 나오면 stack에서 element를 뺌.
- 비슷한 문제로는 백준의 쇠막대기 문제가 있습니다.

3. 알고리즘이 잘 떠오르지 않을 때 : 전역탐색(Brute Force) 
