def solution(s):
    if len(s) == 1:
        return 1
    
    result = 1000
    for length in range(1,len(s)//2 +1):
        s_split = [s[i:i+length] for i in range(0,len(s),length)]
        
        stack = []
        count = 0
        answer = ''
        for alpha in s_split:
            if len(stack)==0:
                stack.append(alpha)
                count+=1
                continue
            
            if stack[-1] == alpha: # 압축하는 경우
                count+=1
            else: # 압축 안되는 경우
                if count > 1:
                    answer+=str(count)+stack[-1]
                else:
                    answer+=stack[-1]
                
                count = 1
                stack.append(alpha)
        if count > 1:
            answer+=str(count)+stack[-1]
        else:
            answer+=stack[-1]
        
        result = min(result, len(answer))
        
    return result