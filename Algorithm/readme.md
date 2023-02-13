1. 시간복잡도 고려.
  - 상수는 무시. O(3N) = O(N)
  - Big O 표기법(최악일 때 시간복잡도)를 고려

2. 문자열 뒤집기 3가지 방법
  - reversed()
  - a.reverse()
  - list[::-1]
  
3. stack , queue -> from collections import deque 무조건 기억.  
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
  
# 다시 풀어볼 문제
1. 분수의 덧셈
