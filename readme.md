# 알고리즘 설계 Tip
연산 횟수 5억 이상
- C++ : 1~3초
- python : 5~15초

**코테 시간제한은 통상 1~5초 가량**
데이터개수(N)개 일 때.
- N < 500 : O(N**3)
- 500 < N < 2000 : O(N**2)
- 2,000 < N < 100,000 : O(N logN)
- 100,000 < N < 10,000,000 : O(N)  
이정도면 풀 수 있음.

## 파이썬 자료형 : int, float, str, list, tuple, dict, set
- int(정수형) : 양/음수
- float(실수형) : 이때 컴퓨터는 2진법이므로 사소한 오류가 있을 수 있다. 이는 1/3을 10진법으로 표현할 수 없는 것과 같은 개념.
  - 개발과정에서 이런 손실값으로 인한 에러를 방지하기 위해 round() 함수를 사용해주는 것이 좋다.
~~~
a = 0.3 + 0.6
print(a) #0.89999999
print(round(a,4)) #0.9
~~~
- str(문자형) : 더하기 연산 가능, index 0부터, slicing 기법
- list(배열) : index는 0부터, slicing 기법, **comprehension**
  - 사용가능한 내장 함수 : .append(), .pop(), .sort(), .reverse(), .count(), .remove(), .insert(index, value)
  - ~~~
    a = [1,2,3,4,5,5,5]
    remove_set = {3,5}

    result = [i for i in a if i not in remove_set]
    print(result) #[1,2,4] 즉 원하는 값 모두 제거.
    ~~~

- tuple(튜플) : list랑 흡사하지만 값 수정이 안됨(=메모리를 효율적으로 관리하기 위해 사용)
- dict(사전 자료형) : key:value로 저장
  - .keys(), .values(), .items()
- set(집합 자료형) : 중복 x, 순서 x(데이터 조회, 수정은 O(1))
  - a|b(합집합), a&b(교집합), a-b(차집합) 연산 지원
  - .add(value), .update([value1, value2]), .remove(value)

## 파이썬 꼭 익혀야할 기본 함수, 표준 라이브러리
- map()
- lambda x:x[1]
- sorted()
- sum()
~~~
import heapq #heap 자료구조
import bisect #이진탐색
import math 

from itertools import permutations, combinations, product, combinations_with_replacement #순열, 조합, 중복허용 순열, 중복허용 조합
from collections import deque, Counter #queue 자료구조, 객체 내 원소 개수 세기.
from math import gcd #최대 공약수
~~~

