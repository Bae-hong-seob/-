from collections import deque

def check_s(s):
    dq = []
    
    for check in s:
        if check=='(' or check=='{' or check=='[':
            dq.append(check)
        else:
            if len(dq)==0:
                return 0
            pair = dq.pop()

            if check==')' and pair != '(':
                return 0
            elif check=='}' and pair != '{':
                return 0
            elif check==']' and pair != '[':
                return 0
            
    if len(dq)==0:
        return 1
    else:
        return 0

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        s = s[1:]+s[0]
        answer+=check_s(s)
    
    return answer