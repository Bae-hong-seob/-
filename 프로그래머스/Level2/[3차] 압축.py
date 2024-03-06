def solution(msg):
    dictionary = {}
    i=1
    for char in range(ord('A'), ord('Z')+1): #사전 초기화
        dictionary[chr(char)] = i
        i+=1
    
    answers, answer = [], 0
    while msg: #최대 1000번.
        now = ''
        for idx, char in enumerate(msg): #최대 1000번 -> 1,000,000번. 완전탐색 가능
            now+=char
            try:
                answer = dictionary[now] #answer에 색인 번호 저장
                if idx == len(msg)-1:
                    answers.append(answer)
                    return answers
                continue
            except: #사전에 등록되지 않은 번호인 경우
                dictionary[now] = i
                i+=1
                msg = msg[len(now)-1:]
                break
        answers.append(answer)
                
    return answers