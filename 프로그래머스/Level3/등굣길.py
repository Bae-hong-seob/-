def solution(m, n, puddles):
    dp_table = [[1]*m for _ in range(n)]
    for column,row in puddles:
        if row-1==0: #맨 위줄에 웅덩이가 존재하는 경우 그 이후 맨 윗줄은 가지 못함
            for i in range(column-1, m):
                dp_table[row-1][i] = 0
        
        elif column-1==0: #맨 왼쪽줄에 웅덩이가 존재하는 경우 그 아래로는 가지 못함
            for i in range(row-1, n):
                dp_table[i][column-1] = 0
        
        else:
            dp_table[row-1][column-1] = 0
        
#     for row in dp_table:
#         print(row)
        
    for row in range(1, n):
        for column in range(1, m):
            if dp_table[row][column]==0:
                continue
            
            dp_table[row][column] = dp_table[row-1][column] + dp_table[row][column-1]
    
    return dp_table[n-1][m-1] % 1000000007