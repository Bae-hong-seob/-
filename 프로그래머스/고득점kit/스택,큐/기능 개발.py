def solution(progresses, speeds):
    number_of_works = len(progresses)
    days = []
    for i in range(number_of_works):
        progress, speed = progresses[i], speeds[i]
        left_progress = 100 - progress
        
        day = (left_progress//speed) + (1 if left_progress%speed != 0 else 0)
        days.append(day)
    
    answer = []
    now, count = days[0], 1
    for day in days[1:]:
        if now < day: #다음 기능이 더 오래걸리는 경우
            answer.append(count)
            now, count = day, 1
        else:
            count+=1
            
    if count!=0:
        answer.append(count)
        
    return answer