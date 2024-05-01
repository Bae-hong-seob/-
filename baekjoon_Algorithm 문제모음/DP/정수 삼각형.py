N = 5
triangle = [
    [7],
    [3,8],
    [8,1,0],
    [2,7,4,4],
    [4,5,2,6,5]
]

N=int(input())
triangle=[]
for _ in range(N):
    triangle.append(list(map(int,input().split())))

dp_table = [[0]*i for i in range(1,N+1)]
dp_table[0][0]=triangle[0][0] #start point

dcolumn=[-1,0] #왼쪽 대각선 또는 오른쪽 대각선에서 내려옴
for row in range(1,N):
    for column,value in enumerate(triangle[row]):
        for i in range(2):
            n_column=column+dcolumn[i]
            if 0<=row-1<N and 0<=n_column<row:
                dp_table[row][column]=max(dp_table[row][column], dp_table[row-1][n_column]+triangle[row][column])

for row in dp_table:
    print(row)
print(max(dp_table[-1]))