from collections import deque

def solution(numbers, target):
    dq = deque([])
    dq.append(numbers[0])
    
    for idx, number in enumerate(numbers):
        if idx == 0:
            continue
        
        for _ in range(len(dq)):
            now = dq.popleft()
            dq.append(now+number)
            dq.append(now-number)
            
    answer = sum([1 for number in dq if number == target])
    
    dq = deque([])
    dq.append(-numbers[0])
    for idx, number in enumerate(numbers):
        if idx == 0:
            continue
        
        for _ in range(len(dq)):
            now = dq.popleft()
            dq.append(now+number)
            dq.append(now-number)
            
    answer += sum([1 for number in dq if number == target])
    return answer