from collections import deque

def solution(numbers):
    dq = deque()
    
    answer = []
    for idx, number in enumerate(numbers): #최대 1,000,000번
        if not dq:
            dq.append([idx, number])
            continue
        
        if dq[-1][1] < number: #최대 dq길이. dq길이 + idx = len(numbers)
            while dq and dq[-1][1] < number:
                index, now_number = dq.pop()
                answer.append([index, now_number, number])
        dq.append([idx, number])

    
    while dq:
        index, now_number = dq.pop()
        answer.append([index, now_number, -1])
    answer.sort()
    return [i[2] for i in answer]