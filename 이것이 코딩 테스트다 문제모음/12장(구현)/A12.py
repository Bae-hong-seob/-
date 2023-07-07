def possible(answer):
    for x,y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            else:
                return False
            
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝 부분이 기둥 위' 혹은 '양쪽 끝 부분이 다른 보와 동시에 연결'이라면 정상
            if [x,y-1,0] in answer or [x+1, y-1, 0] in answer or ([x-1,y,1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
            
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
        x,y,stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x,y,stuff]) # 일단 삭제
            if not possible(answer): # 삭제 불가능하면 다시 복구
                answer.append([x,y,stuff])
                
        else: # 설치하는 경우
            answer.append([x,y,stuff]) # 일단 설치
            if not possible(answer): # 설치 불가능하면 다시 삭제
                answer.remove([x,y,stuff])
    return sorted(answer)