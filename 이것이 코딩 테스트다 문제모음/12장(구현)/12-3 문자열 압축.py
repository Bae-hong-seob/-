def solution(s):
    candidates = []
    
    for length in range(1,(len(s)//2)+1): ## 절반길이까지만 테스트해보면 됨.
        candidate = [s[i:i+length] for i in range(0,len(s),length)]
        stacks = []
        for i in candidate:
            if len(stacks) == 0:
                stacks.append([i,1])
            elif stacks[-1][0] == i: # 연속되는 경우
                count = stacks[-1][1] +1
                stacks.pop()
                stacks.append([i,count])
            else:
                stacks.append([i,1])
        
        encode = ''
        for stack in stacks:
            if stack[1] == 1: # 한 개인 경우 그냥 더하기
                encode+=stack[0]
            else:
                encode+=str(stack[1])+stack[0]
                
        candidates.append(encode)
    
    answers = [len(i) for i in candidates]
    answers.append(len(s)) # 절반 길이만 고려하였으므로 전체 길이를 고려
    
    return min(answers)