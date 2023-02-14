def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    receive=[]
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            receive.append(i)
    
    lost = [i for i in lost if i not in receive]
    
    receive=[]
    for i in lost:
        if i-1 in reserve:
            receive.append(i)
            reserve.remove(i-1)
            continue
        elif i+1 in reserve:
            receive.append(i)
            reserve.remove(i+1)
            continue
        else:
            continue
    return n - len(lost) + len(receive)