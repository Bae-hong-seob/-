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
    for frame in build_frame:
        x,y,a,b = frame # x,y좌표 a 구조물 종류, b 설치/삭제
        
        if b == 1: # 구조물 추가
            answer.append([x,y,a])
            if check_available(answer):
                continue
            else:
                answer.remove([x,y,a])
                
        else: #구조물 삭제
            answer.remove([x,y,a])
            if check_available(answer):
                continue
            else:
                answer.append([x,y,a])
    
    answer = sorted(answer)
    return answer