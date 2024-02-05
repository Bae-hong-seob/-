from collections import deque

def solution(priorities, location):
    max_prior = max(priorities)
    priorities = [[prior, idx] for idx, prior in enumerate(priorities)]
    priorities = deque(priorities)
    
    count = 1
    while priorities:
        prior, idx = priorities.popleft()
        
        if prior == max_prior: #프로세스 실행
            if idx == location:
                return count
            else:
                max_prior = max([prior for prior, idx in priorities])
                count+=1
                continue
        else:
            priorities.append([prior, idx])
    
    return count