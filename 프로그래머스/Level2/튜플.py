import heapq

def solution(s):
    stack, dataset = [], []
    for char in s:
        if char == '{':
            continue
        elif char == '}':
            dataset.append(''.join(stack))
            stack = []
        else:
            stack.append(char)
        
    heap = []
    for subset in dataset:
        if subset == '':
            continue
        elif subset[0] == ',':
            subset=subset[1:]
        heapq.heappush(heap, [len(subset), subset])
    
    answer = []
    while heap:
        length, now = heapq.heappop(heap)
        for char in now.split(','):
            if int(char) not in answer:
                answer.append(int(char))
    return answer