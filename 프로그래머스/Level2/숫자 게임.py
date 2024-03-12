from collections import deque

def solution(A, B):
    A.sort(), B.sort()
    A, B = deque(A), deque(B)
    
    answer=0
    while A and B:
        if A[0] < B[0]:
            answer+=1
            A.popleft()
            B.popleft()
        else:
            B.popleft()
            
    return answer
            