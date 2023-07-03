N = 5 # 공간의 크기 (1<= N <= 100)
moves = ['R', 'R', 'R', 'U', 'D', 'D'] # 1 <= 이동 경로 <= 100

# solution
now = [1,1] # 사용자 출발 위치

for move in moves:
            if move == 'L' and now[1] > 1:
                        now[1]-=1
            elif move == 'R' and now[1] < N:
                        now[1]+=1
            elif move == 'U' and now[0] >1:
                        now[0]-=1
            elif move == 'D' and now[0] < N: # move == 'D'
                        now[0]+=1
            else:
                        continue
            print(now)
