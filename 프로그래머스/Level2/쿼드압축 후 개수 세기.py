from collections import deque
import numpy as np

def pressure(arr):
    count = 0
    for row in arr: # 최대 1024번 반복.
        count+=sum(row)
    if count == len(arr)**2 or count == 0:
        return True
    else:
        return False
        

def solution(arr):
    dq = deque([arr])
    
    zero, one = 0,0
    while dq: #1024 = 2**10. 즉 최대 4구역씩 10번 생성될 수 있음. 4**10 = 1,048,576
        now_arr = dq.popleft()
        N = len(now_arr)
        
        if pressure(now_arr): #최대 1024번 -> 
            if now_arr[0][0] == 0:
                zero+=1
            else:
                one+=1
                
        else:
            now_arr = np.array(now_arr)
            region1, region2, region3, region4 = now_arr[:N//2, :N//2], now_arr[:N//2, N//2:], now_arr[N//2:, :N//2], now_arr[N//2:, N//2:]
            dq.append(region1)
            dq.append(region2)
            dq.append(region3)
            dq.append(region4)

            
    return [zero, one]