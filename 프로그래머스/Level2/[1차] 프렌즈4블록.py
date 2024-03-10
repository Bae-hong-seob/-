def check(board,row, column):
    now=board[row][column]
    if now == '0':
        return False
    
    m,n = len(board), len(board[0])
    
    if row+1 < m and column+1 < n:
        right,down,rightNdown = board[row][column+1], board[row+1][column], board[row+1][column+1]
    else:
        return False
    
    if right==now and down==now and rightNdown==now:
        return True
    else:
        return False
    
def change(board, row,column):
    for i in reversed(range(row)):
        board[i+1][column] = board[i][column]
        board[i][column] = '0'
    

def solution(m, n, board):
    board = [list(row) for row in board]
    # for row in board:
    #     print(row)
    
    count=0
    while True:
        answer=[]
        for row in range(m): #최대 30
            for column in range(n): #최대 30 -> 900번.
                if check(board, row,column):
                    answer.append([row,column])
        
        if len(answer)==0:
            break
        for row,column in answer: #최대 900개.
            count+=sum([board[row][column]!='0',board[row][column+1]!='0',board[row+1][column]!='0',board[row+1][column+1]!='0',])
            board[row][column], board[row][column+1], board[row+1][column], board[row+1][column+1] = '0','0','0','0'

        # print(answer)
        # for row in board:
        #     print(row)

        for row in range(m): #최대 900개
            for column in range(n):
                if row+1 < m and board[row+1][column]=='0': # 아래 빈 공간이 존재하는 경우 떨어진다.
                    board[row+1][column] = board[row][column]
                    board[row][column] = '0'
                    change(board, row,column)

        # print()
        # for row in board:
        #     print(row)
        
        
    return count