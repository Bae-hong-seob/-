from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1,sum2 = sum(queue1), sum(queue2)
    max_iter = len(queue1)*3+1
    
    answer = 0
    for _ in range(max_iter+1):
        if sum1 == sum2:
            break
            
        if sum1 > sum2:
            value = queue1.popleft()
            queue2.append(value)
            sum1-=value
            sum2+=value
            
            answer+=1
        else:
            value = queue2.popleft()
            queue1.append(value)
            sum1+=value
            sum2-=value
            
            answer+=1
        
    
    if answer > max_iter:
        return -1
    else:
        return answer