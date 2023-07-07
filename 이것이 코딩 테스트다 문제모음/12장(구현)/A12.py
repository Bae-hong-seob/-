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

def check_available(answer): # 전체 answer에 대해 가능한 구조물인지 확인
    
    for x,y,a in answer: 
        if a == 0: # 구조물이 기둥일 때 설치가능하려면
            if y > 0: # 2층 이상일 때는 아래에 기둥 또는 왼쪽 또는 오른쪽에 보가 존재해야함.
                down,left,right = [x,y-1,0], [x-1,y,1], [x,y,1]
                if down in answer or left in answer or right in answer:
                    continue
                else:
                    return False
            else:
                continue
            
        else: # 구조물이 보 일 경우
            left_down, right_down = [x,y-1,0], [x+1,y-1,0]
            left, right = [x-1,y,1], [x+1,y,1]
            # 밑에가 기둥 or 양쪽 끝부분이 다른 보와 동시에 연결되어 있는 경우 = 설치가능
            if left_down in answer or right_down in answer or (left in answer and right in answer):
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
            if not check_available(answer): # 삭제 불가능하면 다시 복구
                answer.append([x,y,stuff])
                
        else: # 설치하는 경우
            answer.append([x,y,stuff]) # 일단 설치
            if not possible(answer): # 설치 불가능하면 다시 삭제
                answer.remove([x,y,stuff])
    return sorted(answer)