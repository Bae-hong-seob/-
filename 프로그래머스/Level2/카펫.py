def solution(brown, yellow):
    row,col = 0,0
    print(yellow)
    if yellow == 1:
        col, row = 1,1
        return [3,3]
    elif yellow == 2:
        col, row = 2,1
        return [4,3]
    else:
        col_list = []
        row_list = []
        
    for i in range(1,yellow//2+1):
        if (yellow % i) == 0:
            if i <= yellow // i:
                row_list.append(i)
                col_list.append(yellow // i)
    
    for i in range(len(col_list)):
        col = col_list[i]
        row = row_list[i]
        
        num = col*2 + row*2 + 4
        if num == brown:
            return [col+2, row+2]
        else:
            continue