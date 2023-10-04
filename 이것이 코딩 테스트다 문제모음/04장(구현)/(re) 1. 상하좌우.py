N = 5
moves = ['R', 'R', 'R', 'U', 'D', 'D']

start = [1,1]

for move in moves:
    if move == 'L':
        drow, dcolumn = start[0], start[1]-1
        if dcolumn > 0:
            start = [drow,dcolumn]
    
    if move == 'R':
        drow, dcolumn = start[0], start[1]+1
        if dcolumn < N:
            start = [drow,dcolumn]
    
    if move == 'U':
        drow, dcolumn = start[0]-1, start[1]
        if drow > 0:
            start = [drow, dcolumn]
    
    if move == 'D':
        drow, dcolumn = start[0]+1, start[1]
        if drow < N:
            start = [drow, dcolumn]
            
print(start[0], start[1])