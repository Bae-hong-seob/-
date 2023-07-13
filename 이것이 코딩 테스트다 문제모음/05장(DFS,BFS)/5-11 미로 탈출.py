N,M = 5,6 # N은 세로 M은 가로
graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]
visited = [[False]*M for _ in range(N)]

from collections import deque

def bfs(graph, queue, visited):
    number_of_paths = 0
    while queue:
        try:
            # print()
            # print(queue)
            
            now_row,now_column = queue[0]
            visited[now_row][now_column] = True
            number_of_paths+=1

            print('now position',now_row, now_column)
            
            # 방문해야할 노드 추가
            if now_row + 1 < N:
                if graph[now_row+1][now_column] >= 1 and visited[now_row+1][now_column] == False: # 아래방향에 괴물이 없는 경우 & 방문한 적 없는 노드
                    # print('append : ', now_row+1, now_column)
                    visited[now_row+1][now_column] = True
                    queue.append([now_row+1, now_column])
            if now_column+1 < M:
                if graph[now_row][now_column+1] >= 1 and visited[now_row][now_column+1] == False:# 오른쪽에 괴물이 없는 경우 & 방문한 적 없는 노드
                    # print('append : ', now_row, now_column+1)
                    visited[now_row][now_column+1] = True
                    queue.append([now_row, now_column+1])
            
            # 현재 노드에 대하여 최소 경로 업데이트
            past_row, past_column = queue.popleft()
            graph[now_row][now_column] = min(graph[now_row][now_column], graph[past_row][past_column]+1) # 최소 경로 업데이트
        except:
            print(number_of_paths)
        
    return number_of_paths

queue = deque()
queue.append([3,0])

number_of_paths = bfs(graph, queue, visited)
print(number_of_paths)
print(graph[N-1][M-1])