def solution(n):
    '''
    1에서 n까지 1줄씩 (n개)
    n에서 2n-1까지 진행 (n개)
    2n-1에서 3n-3까지 진행 (n-1개)
    3n-3에서 4n-6까지 진행(n-2개)
    ...
    (1개)
    
    '''
    pyramid = [[0] for i in range(1,n+1)]
    for i in range(1,n+1):
        pyramid[i-1][0] = i
    
    now_number, loop, floor = n+1,0,n-1
    share = 0
    for length in range(n-1,0,-1): #n은 최대 1,000
        numbers = [i for i in range(now_number, now_number+length)]
        now_number = numbers[-1]+1
        #print(length, numbers)
        
        if loop%3==0: # floor층에 일열로 삽입
            if len(pyramid[floor])==1:
                pyramid[floor].extend(numbers)
            else:
                pyramid[floor] = pyramid[floor][:share+1] + numbers + pyramid[floor][share+1:]
            
        elif loop%3==1: #위로 삽입
            for number in numbers: #최대 1,000 -> 1,000,000번. 완전탐색 가능.
                floor-=1
                if loop > 2:
                    pyramid[floor] = pyramid[floor][:-share] + [number] + pyramid[floor][-share:]
                else:
                    pyramid[floor].append(number)
        else: #아래로 삽입
            share+=1
            for number in numbers:
                floor+=1
                pyramid[floor] = pyramid[floor][:share] + [number] + pyramid[floor][share:]
        
        loop+=1
    
    # print()
    # for row in pyramid:
    #     print(row)
        
    answer = []
    for row in pyramid:
        answer.extend(row)
    return answer
