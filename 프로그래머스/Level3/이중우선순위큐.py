import heapq

def solution(operations):
    
    heap = []
    
    for operation in operations:
        order , value = operation.split()
        if order=='I':
            heapq.heappush(heap,int(value))
        else:
            if len(heap) == 0:
                continue
            
            elif order=='D' and value=='-1': #최솟값 삭제
                heapq.heappop(heap)
            else: #최댓값 삭제 
                heap = [-w for w in heap]
                heapq.heapify(heap)
                heapq.heappop(heap)
                heap = [-w for w in heap]
                heapq.heapify(heap)
    
    heap.sort()
    
    if len(heap)==0:
        return [0,0]
    else:
        return [heap[-1], heap[0]]