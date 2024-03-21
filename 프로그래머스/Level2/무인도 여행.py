from collections import deque

def solution(maps):
    maps = [list(row) for row in maps]
    # for row in maps:
    #     print(row)
    
    m,n = len(maps), len(maps[0])
    answer = []
    for row in range(m): #최대 100
        for column in range(n): #최대 100 -> 10,000번.
            if maps[row][column] != 'X':
                queue = deque()
                queue.append([row,column])
                result = 0
                while queue:
                    now_row, now_column = queue.popleft()
                    if maps[now_row][now_column] == 'X': #방문한 적이 있으면 패스
                        continue
                    result+=int(maps[now_row][now_column])
                    maps[now_row][now_column] = 'X' #방문처리
                    
                    #오른쪽 탐색
                    if now_column+1<n and maps[now_row][now_column+1] != 'X':
                        queue.append([now_row, now_column+1])
                    
                    #위쪽 탐색
                    if now_row-1>=0 and maps[now_row-1][now_column] != 'X':
                        queue.append([now_row-1, now_column])
                        
                    #왼쪽 탐색
                    if now_column-1>=0 and maps[now_row][now_column-1] != 'X':
                        queue.append([now_row, now_column-1])
                        
                    #아래쪽 탐색
                    if now_row+1<m and maps[now_row+1][now_column] != 'X':
                        queue.append([now_row+1, now_column])
                        
                answer.append(result)
                
                
    if answer:
        return sorted(answer)
    else:
        return [-1]