N, M = 4,4 # N >= 3, M <= 50 (N,M 맵크기)
A,B,d = 1,1,0 # (A,B)는 캐릭터 위치, d는 direction(0,1,2,3) 순서대로 북,동,남,서

map = [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]] # 0은 육지, 1은 바다.

# solution
visited = [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]]
visited[A][B] = 1

count = 0

# N이 row(=y), M이 column(=x)
while(True):
            now_d = d
            
            for i in range(4): # 방향은 4개 중에 하나
                        d = (d-1) % 4
                        new_y,new_x = A,B
                        if d == 0: # 북쪽
                                    new_y -= 1
                        elif d == 1: # 동쪽
                                    new_x += 1
                        elif d == 2: # 남쪽
                                    new_y += 1
                        elif d == 3: # 서쪽
                                    new_x -= 1
                        else:
                                    print('error')
                                    break
                        
                        if new_x >= M or new_x < 0 or new_y >= N or new_y < 0: # map을 벗어난 경우
                                    continue
                        print(d,new_x, new_y)
                        print('visited', visited[new_y][new_x])
                        
                        if visited[new_y][new_x] == 0: # 육지이고, 가본적 없는 곳.
                                    A, B = new_y,new_x # 현재 위치 업데이트
                                    visited[new_y][new_x] = 1 # 가본곳으로 map 업데이트
                                    count+=1

                                    break
            print('Direction',now_d, d)
            
            if now_d == d: #네 방향 모두 이동할 수 없는 경우
                        back_d = (d-2) % 4
                        new_y,new_x = A,B
                        if back_d == 0: # 북쪽
                                    new_y -= 1
                        elif back_d == 1: # 동쪽
                                    new_x += 1
                        elif back_d == 2: # 남쪽
                                    new_y += 1
                        elif back_d == 3: # 서쪽
                                    new_x -= 1
                        else:
                                    print('error')
                                    break

                        if map[new_y][new_x] == 1: # 뒤쪽 방향이 바다라 갈 수 없을 때 반복문 종료
                                    break
                        else: #뒤로 돌아가는 경우
                                    A,B = new_y,new_x #현재 위치 업데이트
                                    count+=1
                                    
print(count)