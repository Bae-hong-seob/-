from collections import deque

def solution(order):
    order = deque(order)
    boxes = [i for i in range(1,len(order)+1)]
    
    container, answer = [],[]
    for i in range(1, len(order)+1): #최대 1,000,000번
        #print(i, container, answer)
        if i == order[0]:
            answer.append(order.popleft())
        else:
            container.append(i)
            
        if container and order[0] == container[-1]:
            while container and order[0] == container[-1]:
                answer.append(container.pop())
                order.popleft()

    
    
    while order: #최대 1,000,000번.
        #print(order, container, answer)
        now = order.popleft()
        if container and container[-1] == now:
            answer.append(container.pop())
        else:
            break
            
    return len(answer)