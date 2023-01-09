from collections import deque

def solution(s):
    i = 0
    j = 0
    dq=deque() # 덱 생성
    dq.append(s[i])
    i+=1
    
    while(i != len(s)):
        if len(dq) == 0:
            dq.append(s[i])
            i+=1
        elif dq[-1] == s[i]:
            dq.pop()
            i+=1
        else:
            dq.append(s[i])
            i+=1
            
    if len(dq)== 0:
        return 1
    else:
        return 0
        
        
        