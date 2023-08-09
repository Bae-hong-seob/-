# N = 7 # 1 <= N <= 2000
# points = [15, 11, 4, 8, 5, 2, 4]

N = int(input())
points = list(map(int, input().split()))

dp_table = [1 for _ in range(N)]

for idx, point in enumerate(points):
    if idx == 0 or idx == N-1: # 시작과 끝이라면 종료
        continue
    
    if points[idx] >= points[idx+1]: # 길이 증가 시
        dp_table[idx] = max(dp_table[idx], max([dp_table[j]+1 for j in range(idx)]))
        
    
#print(dp_table)
print(N - max(dp_table) -1) # 맨 마지막 길이도 포함시켜야하는데 못함.