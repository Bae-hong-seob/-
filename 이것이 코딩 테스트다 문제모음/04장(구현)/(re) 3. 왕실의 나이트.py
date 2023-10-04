point = 'a1'

row, column = point[1], point[0]
columns = [0, 'a','b','c','d','e','f','g','h']
column = columns.index(column)
row, column = int(row), int(column)

moves = [ # [row, column]
    [-1,2], [1,2], # right
    [2,-1], [2,1], # down
    [-1,-2],[1,-2], # left
    [-2,-1],[-2,1] # up
]

count = 0
for move in moves:
    drow, dcolumn = move
    new_row, new_column = row+drow, column+dcolumn
    
    if new_row > 0 and new_row < 9 and new_column > 0 and new_column < 9:
        count+=1
        
print(count)