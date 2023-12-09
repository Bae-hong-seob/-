import numpy as np
import copy

def rotation(original):
    n = len(original)
    m = len(original[0])
    
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][i] = original[n-i-1][j]
            
    return result

def solution(key, lock):
    N,M = len(lock), len(key)
    extension_lock = [[0]*3*N for _ in range(3*N)]
    extension_lock, lock, key = np.array(extension_lock), np.array(lock), np.array(key)
    extension_lock[N:N+N, N:N+N] = lock
    
    # for row in extension_lock:
    #     print(row)
    # print()
    
    for _ in range(4): #90도 회전 4번
        key = rotation(key)
        
        for row in range(N*3-M):
            for column in range(N*3-M):
                tmp_extension_lock = copy.deepcopy(extension_lock)
                tmp_extension_lock[row:row+M, column:column+M] += key
                
                if np.max(tmp_extension_lock) == 1 and np.sum(tmp_extension_lock[N:N+N, N:N+N]) == N*N:
                    return True
                
                if all(i==1 for i in tmp_extension_lock[N:N+N, N:N+N].reshape(-1)):
                    return True
                
                # if row < N and column < M:
                #     for value in tmp_extension_lock:
                #         print(value)
                #     print()
                    
    return False