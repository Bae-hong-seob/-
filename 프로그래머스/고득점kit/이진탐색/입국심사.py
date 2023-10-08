import heapq

def solution(n, times): # 시간초과
    if n <= len(times): # 심사인원보다 심사관이 많은 경우
        return max(times)
    
    time_idx = []
    for time in times:
        time_idx.append((time*2,time,1)) #(end, start, idx)
        
    heapq.heapify(time_idx)
    n-=len(times) # 첫 배정
    
    for _ in range(n):
        #print(time_idx)
        end, start, idx = heapq.heappop(time_idx)
        gap = end-start
        heapq.heappush(time_idx, (gap*(idx+2),gap*(idx+1),idx+1))
        
    return end

def solution(n, times): # 성공
    start, end = 0, max(times)*n
    while start <= end:
        mid = (start+end)//2
        people = 0
        for time in times:
            people += (mid//time) # 총 시간이 주어졌을 때 심사관 한명이 담당할 수 있는 사람 수
            if people >=n:
                break

        if people >= n: # 시간이 너무 충분하게 주어진 경우
            answer = mid
            end = mid-1
        elif people < n: # 시간이 너무 부족한 경우
            start = mid+1
            
    return answer