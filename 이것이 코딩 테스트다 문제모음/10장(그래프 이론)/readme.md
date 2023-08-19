# 10장

그래프 : 인접행렬 혹은 인접리스트로 표현하기.

탐색 알고리즘
1. DFS : stack. index가 작은쪽부터 쭉 탐색하고 올라오기
2. BFS : q -> import deque.

탐색 중 최단 경로 알고리즘
1. 다익스트라 : q -> import deque
- i 노드에서 j노드로 가는 경우 : dp_table[i] + distance < dp_table[j] 시 update.
2. 플로이드 워셜 알고리즘 : 3중 for문. k,i,j 순서로 짜기.
- i 노드에서 k노드를 거쳐 j노드로 가는 경우 : dp_table[i][j] = min(dp_table[i][j], dp_table[i][k] + dp_table[k][j])
