# 주요 알고리즘
## 1. DP(Dynamic Programming) 최대값, 최소값 이런거 구하라고 나오면 왠만해서는 DP. 점화식 활용
- 일명 기억하며 풀기. 재귀적인 방법은 O(N**2) -> DP는 O(N)
- DP, 즉 다이나믹 프로그래밍(또는 동적 계획법)은 기본적인 아이디어로 하나의 큰 문제를 여러 개의 작은 문제로 나누어서 그 결과를 저장하여 다시 큰 문제를 해결할 때 사용하는 것으로 특정한 알고리즘이 아닌 하나의 문제해결 패러다임으로 볼 수 있다.
- 큰 문제를 작은 문제로 쪼개서 그 답을 저장해두고 재활용한다. 그래서 혹자는 DP가 아닌 '기억하며 풀기'라고 부르기도 한다.
- 보통 특정 데이터 내 최대화 / 최소화 계산을 하거나 특정 조건 내 데이터를 세야 한다거나 확률 등의 계산의 경우 DP로 풀 수 있는 경우가 많다.

## 2. 부분집합 원소 곱의 최대값
- 일단 외워. 고르게 분포하게 만드는게 최대값이야. 

## 3. DFS, BFS 구현하기
~~~
def dfs(v):
    visited[v] = True

    for nei in range(n):    # 인접노드 탐구 
        if not visited[nei] and computers[v][nei]:    # unvisited + 인접할 때 
            dfs(nei)
~~~

## 4. heapq 구조 사용하기 -> max heapq, min heapq
- heapq 는 일반적으로 가장 작은 value가 root node
- max_heapq를 만들기 위해서는 -value list로 하면된다.
- heapify 이거 생각보다 시간복잡도 큼. O(N)
- heappush, heappop하면 알아서 heap 구조가 유지된다.
~~~
import heapq #import 문에서는 heapq -> q 주의
   
works = [4,3,3] # minheapq
works = [-w for w in works] #max heapq

heapq.heapify(works) #heaq 구조 만들기! #기존 리스트를 heap구조로 초기화 시켜줘야함. & heapq 라이브러리 안에 heapify = heap + ify 기억

i = heapq.heappop(works) #pop(heaq) #heapq 라이브러리 안에 heappop = heap + pop
heapq.heappush(works, i) #push(heaq, value) #heapq 라이브러리 안에 heappush = heap + push

#즉 라이브러리 안에 function 이름들은 q 빠져있음.
~~~

# 다시 풀어볼 문제
1. <s>이중우선순위큐 -> heapq 이용하여 다시 풀어볼 것</s>
- https://littlefoxdiary.tistory.com/3 참고
2. <s>부분집합 원소 곱의 최대값 구하기. 
- 증명해봐. </s> -> 1*(n-1) <= n/2 * n/2 증명가능
3. 네트워크 -> DFS, BFS 두 개다 구현해보고 풀어보기
