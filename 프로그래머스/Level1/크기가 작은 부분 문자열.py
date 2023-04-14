def solution(t, p):
    candidates = []
    for i in range(len(t)):
        candidate = ''
        try: # first p개까지 뒤로 탐색할 수 있을 때
            for j in range(i,i+len(p)):
                candidate+=t[j]
            candidates.append(int(candidate))
        except: # 탐색 안될 때 = 더이상 후보군 없음
            break
            
    answer = 0
    
    for candidate in candidates:
        if candidate <= int(p):
            answer+=1
    return answer