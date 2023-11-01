def check_available(answer):
    for column,row,a in answer:
        if a==0: # 기둥
            if row ==0: #1층에 기둥은 그냥 세울 수 있음
                continue
                
            if [column,row-1,0] in answer or [column-1,row,1] in answer or [column,row,1] in answer: # 2층 이상 기둥은 아래에 기둥이거나, 아래 왼쪽에 보설치 or 아래에 보 설치
                continue
            else:
                return False
            
        elif a==1: # 보
            if [column,row-1,0] in answer or [column+1,row-1,0] in answer or ([column-1,row,1] in answer and [column+1,row,1] in answer): # 아래에 기둥 or 오른쪽 아래에 기둥 or 양쪽에 보
                continue
            else:
                return False
            
    return True

def solution(n, build_frame):
    answer = []
    for column,row,a,b in build_frame:
        if b == 0: # 삭제
            answer.remove([column,row,a])
            if check_available(answer):
                continue
            else:
                answer.append([column,row,a])
        elif b == 1: # 설치
            answer.append([column,row,a])
            if check_available(answer):
                continue
            else:
                answer.remove([column,row,a])
                
    answer.sort()
    return answer