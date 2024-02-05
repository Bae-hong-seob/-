def solution(s):
    stack = []
    answer = True
    for check in s:
        if check == '(':
            stack.append(check)
        else:
            try:
                stack.pop()
            except:
                answer = False
    
    if len(stack) != 0:
        answer = False

    return answer