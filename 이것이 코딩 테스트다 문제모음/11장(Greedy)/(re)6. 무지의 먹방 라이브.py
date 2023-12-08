import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    time_and_index = [[time, idx+1] for idx, time in enumerate(food_times)]
    heapq.heapify(time_and_index)
    
    steps = 0
    while k>0 and time_and_index:
        time, length = time_and_index[0][0], len(time_and_index)
        time_for_delete = (time-steps) * length
        
        if time_for_delete > k: # 음식 다 못먹음
            break
        
        steps += (time-steps)
        k-=time_for_delete
        
        #print(time_and_index, time, steps, length, time_for_delete)
        #print(steps, k)
        
        # 다 먹은 음식 경우 제거
        count = 0
        for ttime,idx in time_and_index:
            if ttime-steps <= 0:
                count+=1
            else:
                break
                
        for _ in range(count):
            heapq.heappop(time_and_index)
            
    #print('result : ', time_and_index)
    
    time_and_index.sort(key=lambda x:x[1])
    return time_and_index[k%len(time_and_index)][1]