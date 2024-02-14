def solution(n, lost, reserve):
    #도난 당한 학생 번호, 여유분 가져온 학생 번호 정렬.
    lost.sort()
    reserve.sort()
    
    new_lost = []
    for empty in lost:
        if empty in reserve:
            reserve.remove(empty)
        else:
            new_lost.append(empty)
    lost = new_lost

    count=0
    for empty in lost:
        if empty-1 in reserve: #되도록 적은쪽 부터 구한다. 
            reserve.remove(empty-1)
        elif empty+1 in reserve:
            reserve.remove(empty+1)
        else: #못빌리는 경우. 못빌리는 학생수(count) 증가
            count+=1
        
    return n-count