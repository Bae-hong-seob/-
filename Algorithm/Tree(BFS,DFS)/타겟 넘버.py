# 너비 우선 탐색(queue) -> leaf node만 남김
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

# 너비 우선 탐색 - 트리를 전체를 구현
# from collections import deque 

# def solution(numbers, target):
    
#     q = deque()
#     count=0
#     n = len(numbers)
    
#     q.append([numbers[0],0])
#     q.append([-numbers[0],0])
    
#     while q:
#         value, idx = q.popleft()
#         idx+=1
#         if idx < n:
#             q.append([value+numbers[idx],idx])
#             q.append([value-numbers[idx],idx])
#         else:
#             if value == target:
#                 count+=1 

#     return count