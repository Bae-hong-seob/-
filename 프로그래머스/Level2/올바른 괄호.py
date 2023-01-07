from collections import deque

def solution(s):
    stack = deque()
    for i in s:
        if i == ')' and not stack:  # 스택에 아무것도 없는데 ')'가 있는 경우
            return False
        elif i == ')' and stack[-1] == '(':  # 괄호쌍 없애줌
            stack.pop()
        else:  # i가 '('일 때
            stack.append(i)
    return True if not stack else False

