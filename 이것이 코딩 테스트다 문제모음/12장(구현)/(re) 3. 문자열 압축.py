def solution(s):
    answers = []
    min_length = len(s)
    for length in range(1,len(s)//2 + 1):
        candidates = [s[i:i+length] for i in range(0,len(s),length)]
        #print(candidates)
        
        prev, count = '', 1
        answer = ''
        for candidate in candidates:
            if prev == candidate: # 압축
                count+=1
                
            else:
                if count > 1:
                    answer+= str(count)+prev
                else:
                    answer+=prev
                    
                prev = candidate # 기준 수정
                count = 1
                
        if count > 1:
            answer+= str(count)+prev
        else:
            answer+=prev
            
        answers.append(answer)
        min_length = min(min_length, len(answer))
    
    # for answer in answers:
    #     print(answer, len(answer))
    
    return min_length