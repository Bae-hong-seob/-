import heapq

def solution(operations):
    heap = []
    for operation in operations: #최대 1,000,000 반복.
        operation, value = operation.split()
        if operation == 'I': #삽입
            heapq.heappush(heap, int(value))
        elif not heap: #구조가 빈 경우 무시
            continue
        elif operation == 'D' and value=='1': #최대값 삭제
            heap = [-value for value in heap] #최대값이 가장 먼저 오도록 구조 수정
            heapq.heapify(heap) 
            heapq.heappop(heap)
            heap = [-value for value in heap] #다시 최소값이 가장 먼저 오는 구조로 복구
            heapq.heapify(heap)
        elif operation == 'D' and value=='-1': #최소값 삭제
            heapq.heappop(heap)
        else:
            print('InputError')
            
    if heap:
        min_value = heap[0]
        heap = [-value for value in heap]
        heapq.heapify(heap)
        max_value = -1 * heap[0]
        return [max_value, min_value]
    else:
        return [0,0]