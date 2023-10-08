def solution(n, lost, reserve):
    after_reserve = []
    after_lost = []
    for check in reserve:
        if check in lost:
            continue
        else: # 여벌이 도난당하지 않았을 때만 여벌이 있는 것으로 update
            after_reserve.append(check)
    
    for check in lost:
        if check in reserve:
            continue
        else: # 도난 당했는데 여벌이 있는 경우 도난 당하지 않은 것으로 update
            after_lost.append(check)
            
    after_reserve.sort()
    after_lost.sort()
    count = 0
    for idx in after_lost:
        if idx-1 in after_reserve: # 왼쪽에 여벌이 있는 경우
            after_reserve.remove(idx-1)
        elif idx+1 in after_reserve: # 왼쪽에는 없고 오른쪽에 여벌이 있는 경우
            after_reserve.remove(idx+1)
        else: # 여벌이 없는 경우
            count+=1
            continue
    
    return n-count