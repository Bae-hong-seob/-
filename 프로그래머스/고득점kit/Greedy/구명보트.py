from collections import deque

def solution(people, limit):
    people.sort()
    dq = deque(people)
    
    number_of_boats = 0
    while dq:
        max_weight = dq.pop()
        if dq and dq[0] + max_weight <= limit: #두명 같이 태울 수 있는 경우
            dq.popleft()
        number_of_boats+=1
        
    return number_of_boats