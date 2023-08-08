# T = 2 # 1 <= T <= 1000
# N,M = 3,4 # 1 <= N,M <= 20
# golds = [
#     [1,3,3,2],
#     [2,1,4,1],
#     [0,6,4,7]
# ]

N,M = 4,4
golds = [
    [1,3,1,5],
    [2,2,4,1],
    [5,0,2,3],
    [0,6,1,2]
]

# DP 테이블 재 구축하는 방식으로 진행. 최대 이익을 해당칸에 저장
dp_table = [[0]*M for _ in range(N)]
print(dp_table)

for row in range(N):
    dp_table[row][0] = golds[row][0]
print(dp_table)

for column in range(1,M):
    for row in range(N):
        if row == 0: # 왼쪽과 왼쪽 아래에서 오는 경우만 고려하면 됨
            dp_table[row][column] = golds[row][column] + max(dp_table[row][column-1], dp_table[row+1][column-1])
            
        elif row == N-1: # 왼쪽과 왼쪽 위에서 오는 경우만 고려하면 됨
            dp_table[row][column] = golds[row][column] + max(dp_table[row][column-1], dp_table[row-1][column-1])
            
        else: # 왼쪽과 왼쪽 위, 왼쪽 아래 세 가지 경우 모두 고려
            dp_table[row][column] = golds[row][column] + max(dp_table[row][column-1], dp_table[row-1][column-1], dp_table[row+1][column-1])
            
print(dp_table)

answer = max([row[-1] for row in dp_table])
print(answer)