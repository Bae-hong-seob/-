from collections import deque

def solution(numbers, target):
    #print(2**20) #완전탐색 시간복잡도 확인. 1,048,576. 완전탐색 가능.
    queue = deque([0])
    
    for number in numbers:
        new_queue = deque()
        while queue:
            now = queue.popleft()
            new_queue.append(now+number)
            new_queue.append(now-number)
        queue = new_queue
        
    queue = list(queue)
    return queue.count(target)
