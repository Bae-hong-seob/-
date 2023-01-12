from collections import deque

def solution(n, words):
    num = 0
    count = 0
    
    dq = deque()
    
    for i in words:
        print(dq)
        num+=1
        if num % n == 1:
            num = 1
            count+=1
            
        if len(dq)==0:
            last = i[-1]
            dq.append(i)
            continue
        elif i in dq:
            return [num,count]
        else:
            first = i[0]
            if last != first:
                return [num,count]
            else:
                last = i[-1]
                dq.append(i)

    return [0,0]