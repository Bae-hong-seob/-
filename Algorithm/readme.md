1. 시간복잡도 고려.
  - 상수는 무시. O(3N) = O(N)
  - Big O 표기법(최악일 때 시간복잡도)를 고려

2. 문자열 뒤집기 3가지 방법
  - reversed()
  - a.reverse()
  - list[::-1]
  
3. key값 기준 정렬
~~~
box = [[0,3],[7,2],[0,10]]
box.sort(key = lambda x: x[1])
~~~

4. 정렬
데이터에 따라 가장 빠른 정렬 알고리즘이 다르다. https://www.toptal.com/developers/sorting-algorithms
 
  - 삽입정렬 : 선택한 요소를 삽입할 수 있는 위치를 찾아 삽입하는 정렬 알고리즘. O(N**2).
    - 단 어느정도 정렬되어 있는 상황에서는 퀵 정렬보다 빠름
  - 버블정렬 : 가장 인접한 요소를 비교하여 
  - 선택정렬 : 선택한 요소와 가장 우선순위가 높은 요소를 교환하는 정렬 알고리즘. O(N**2)

  분산식 정렬 : "분할 정복"  
  - 합병정렬 : 분할 정복 알고리즘을 이용한 최선과 최악이 같은 안정적인 정렬 알고리즘. O(log N)
    - Divide & Conquer
  - 퀵 정렬 : 분할 정복 알고리즘을 이용한 매우 빠르지만 최악의 경우가 존재하는 불안정 정렬. O(log N)

# 알고리즘
1. stack , queue -> from collections import deque 무조건 기억.  
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

2. Greedy -> 직관적인 문제풀이.

3. Graph 
  
# 다시 풀어볼 문제
1. 분수의 덧셈
