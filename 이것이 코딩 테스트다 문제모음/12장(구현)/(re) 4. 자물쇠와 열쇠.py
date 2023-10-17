def rotation(original):
    n = len(original) # 행
    m = len(original[0]) # 열
    
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = original[i][j]
            
    return result
    

def check_unlock(map, tmp_key, lock):
    tmp_map = [row.copy() for row in map]
    for row in range(len(lock), len(lock)*2):
        for column in range(len(lock), len(lock)*2):
            tmp_map[row][column] += tmp_key[row][column]
            
    for row in range(len(lock), len(lock)*2):
        for column in range(len(lock), len(lock)*2):
            if tmp_map[row][column] != 1:
                return False
    
    return True
    

def solution(key, lock):
    map = [[0]*len(lock)*3 for _ in range(len(lock)*3)]
    
    for row in range(len(lock), len(lock)*2):
        for column in range(len(lock), len(lock)*2):
            map[row][column] = lock[row-len(lock)][column-len(lock)]
    
    
    answer = True
    
    for _ in range(4): #90도 회전 4번 레츠고
        key = rotation(key)

        for row in range(0, len(map)-len(key)):
            for column in range(0, len(map)-len(key)):
                tmp_key = [[0]*len(lock)*3 for _ in range(len(lock)*3)]
                for key_row, tmp_row in zip(key,tmp_key[row:row+len(key)]):
                    tmp_row[column:column+len(key)] = key_row

                if check_unlock(map, tmp_key, lock): # 잠금 해제 가능
                    return True

    return False