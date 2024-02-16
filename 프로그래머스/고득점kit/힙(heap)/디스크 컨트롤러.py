import heapq

def solution(jobs):
    heap = []
    heapq.heapify(jobs)
    total, now, n = 0,0,len(jobs)
    
    for i in range(n): #최대 한번에 하나씩 처리. 총 500번 반복
        while jobs and jobs[0][0] <= now: #현재 처리 가능한 요청
            start, consume = heapq.heappop(jobs)
            heapq.heappush(heap,[consume, start])
        
        #현재 처리 가능한 요청이 없는 경우. 기다렸다가 다음 요청 처리
        if not heap and jobs:
            start, consume = heapq.heappop(jobs)
            heapq.heappush(heap, [consume, start])
            now = now+(start-now)
        
        consume, start = heapq.heappop(heap) #쌓인 요청 중 소요시간이 가장 짧은 요청 먼저 처리
        total+= (now-start)+consume #기다린시간 + 소요시간
        now+=consume
        
    
    return int(total/n)