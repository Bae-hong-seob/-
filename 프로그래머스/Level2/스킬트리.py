from collections import deque

def solution(skill, skill_trees):
    
    answer=0
    for skill_tree in skill_trees: #최대 20
        skills = deque(skill) #선행스킬 순서 생성
        skill_tree = deque(skill_tree)
        
        available = True
        while skill_tree: # 최대 26 -> 520번 반복
            now = skill_tree.popleft()
            if now in list(skills): #선행 스킬 순서가 있는 경우
                if now == skills[0]:
                    skills.popleft()
                else:
                    available=False
                    break
            else:
                continue
        
        if available == True:
            answer+=1
            
            
    return answer