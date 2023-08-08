# N = 5 # 삼각형 크기
# triangle = [
#     [7],
#     [3,8],
#     [8,1,0],
#     [2,7,4,4],
#     [4,5,2,6,5]
#     ]

N = int(input())
triangle = []
for _ in range(N):
    triangle.append(list(map(int, input().split())))

dp_table = triangle.copy()
#print(dp_table)

for row in range(1,N):
    for column in range(len(triangle[row])):
        if column == 0: # 오른쪽 대각선만 고려가능
            dp_table[row][column] += dp_table[row-1][column]
            
        elif column == len(triangle[row])-1: # 왼쪽 대각선만 고려가능
            dp_table[row][column] += dp_table[row-1][column-1]
            
        else: # 왼쪽 대각선 오른쪽 대각선 모두 고려
            dp_table[row][column] = max(dp_table[row][column]+dp_table[row-1][column-1], dp_table[row][column]+dp_table[row-1][column])
            
#print(dp_table)
print(max(dp_table[-1]))