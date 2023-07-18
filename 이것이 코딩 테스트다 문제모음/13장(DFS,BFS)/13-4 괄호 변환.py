def check_right(w):
    stack = []
    check_list = w.copy()
    
    while check_list:
        s = check_list.pop(0)
        if s == '(':
            stack.append(s)
        else: # s == ')'
            try:
                stack.pop()
            except:
                return False
    if len(stack) == 0 and len(check_list) == 0:
        return True
    else:
        return False
            
def check_balance(p):
    if p.count('(') == p.count(')'):
        return True
    else:
        return False
    
def split_uv(p): #split u,v
    for idx, value in enumerate(p): 
        #print(idx,value)
        temp = p[:idx+1]
        if temp.count('(') == temp.count(')'):
            u, v = p[:idx+1], p[idx+1:]
            #print(u,v)
            return u,v
    return [],[]

def make_answer(u, answer):
    result = ''
    
    while u:
        u,v = split_uv(u)
        if check_right(u): # u가 올바른 문자열이라면
            result+=''.join(u) # 정답에 추가
            #print('answer :', result)
            u = v # v에 대해 재귀적으로 수행
        
        else: # u가 올바른 문자열이 아니라면
            first = '('
            #print('u, result : ', u, result)
            second = make_answer(v, answer)
            thrid = ')'
            fourth = ''.join(['(' if i == ')' else ')' for i in u[1:-1]])
            result += first+second+thrid+fourth
            #print('result : ', result)
            break
            
    return answer+result
    
def solution(p):
    if len(p) == 0: # 빈 문자열인 경우 빈 문자열을 반환
        return ''
    
    answer = ''
    u = list(p)
    
    if check_right(u):
        return ''.join(u)
    
    answer = make_answer(u, answer)
    return answer