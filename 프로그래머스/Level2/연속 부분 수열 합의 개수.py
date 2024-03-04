from collections import deque

def solution(elements):
    answer = set()
    for length in range(1, len(elements)+1): #최대 1,000번.
        cycle = elements + elements[:length] # 원형 수열 표시
        dq = deque([i for i in cycle[:length]])
        for element in cycle[length:]: # 한칸씩 옮기면서 길이만큼 합을 구함. 최대 1,000번 -> 1,000,000번. 완전탐색 가능
            answer.add(sum(dq))
            dq.popleft()
            dq.append(element)
        
    return len(answer)