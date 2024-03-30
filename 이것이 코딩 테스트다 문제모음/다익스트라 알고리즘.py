n,m = 6, 11 
# 시작 노드 번호를 입력받기
start = 1
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기 -> 인접리스트로 구현
graph = [[],
         [(2,2),(3,5),(4,1)],
         [(3,3),(4,2)],
         [(2,3),(6,5)],
         [(3,3),(5,1)],
         [(3,1),(6,2)],
         [],
         ]

import heapq

'''
문제: 1번 노드에서 다른 모든 노드로 이동하는 최단경로 구하기
'''

INF = int(1e9)
distances = [INF]*(n+1)

distances[start] = 0 #시작은 거리 0으로 초기화

heap = [[0,start]]

while heap:
    cost, node_idx = heapq.heappop(heap)
    print(cost, node_idx)
    
    if distances[node_idx] < cost:
        continue
    
    for neighbor_idx,next_cost in graph[node_idx]:
        if cost+next_cost < distances[neighbor_idx]:
            distances[neighbor_idx] = cost+next_cost
            heapq.heappush(heap, [cost+next_cost, neighbor_idx])

print(distances)