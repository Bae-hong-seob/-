# 너비 우선 탐색(queue)
from collections import deque
def solution(numbers, target):
    tree = deque()
    n = 0
    for i in numbers:
        plus, minus = i, -i
        if len(tree)==0:
            tree.append(plus)
            tree.append(minus)
        else:
            for _ in range(2**n):
                x = tree.popleft()
                tree.append(x+plus)
                tree.append(x+minus)
        n+=1
    answer = 0
    return tree.count(target)