from collections import deque

def solution(priorities, location):
    
    dq =deque()
    priorities = deque(priorities)
    
    while(priorities):
        j = priorities[0]
        if j == max(priorities):
            dq.append(priorities.popleft())
            if location==0:
                return len(dq)
            else: location-=1
            
            if location<0:
                location=len(priorities)-1
        else:
            priorities.append(priorities.popleft())
            location-=1
            if location <0:
                location = len(priorities)-1