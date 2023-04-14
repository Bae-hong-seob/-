from collections import deque

def solution(progresses, speeds):
    dq = deque()
    answer = []
    
    for progress, speed in zip(progresses, speeds):
        if (100 - progress)%speed == 0:
            day = (100 - progress)//speed
        else:
            day = (100 - progress)//speed + 1
            
        if len(dq)==0:
            dq.append([progress,speed,day])
        elif dq[-1][2] >= day: #stack 쌓이는중 day는 이전껄로 유지
            dq.append([progress,speed,dq[-1][2]])
        else: #dq clear & 새로 stack
            answer.append(len(dq))
            dq.clear()
            dq.append([progress,speed,day])
    
    answer.append(len(dq))
    return answer