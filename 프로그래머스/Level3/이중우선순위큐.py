def solution(operations):
    dq = []
    for i in operations:
        order, num = i.split()
        if order=='I':
            dq.append(int(num))
        elif len(dq)==0:
            continue
        else:
            if num == '1':
                dq.pop(dq.index(max(dq)))
            else:
                dq.pop(dq.index(min(dq)))
                
    if len(dq)==0:
        return [0,0]
    else:
        return [max(dq),min(dq)]