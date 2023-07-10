1. 완전 탐색
- 반복문, 재귀 함수 사용하여 에외 케이스 모두 확인
- DFS/BFS 알고리즘 이용
2. 시뮬레이션


구현 : 구현해야 할 소스코드의 양이 매우 많은 문제도 출제.

~~~
# 문자를 하나씩 확인하며
for x in data:
            # 알파벳인 경우 결과 리스트에 삽입
            if x.isalpha():
                        result.append(x)
            else:
                        value+=int(x)
~~~

부분집합 구하기
~~~
from itertools import combinations 

arr = [1,2,3]

print(list(combinations(arr,1)))
#[(1,), (2,), (3,)]
~~~
