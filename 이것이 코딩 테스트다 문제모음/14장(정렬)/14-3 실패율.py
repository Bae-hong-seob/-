def solution(N, stages):
    stack = [0 for _ in range(N+2)]

    for stage in stages:
        stack[stage]+=1
    
    answer = []
    for idx, number_of_users in enumerate(stack):
        if idx == 0: # stage 0 은 없음.
            continue
        if idx == N+1: # 마지막 스테이지까지 클리어한 사용자
            break
            
        total_number_of_users = sum(stack[idx:]) # 총 도전자 수
        try:
            fail_rate = number_of_users / total_number_of_users
            answer.append([idx, fail_rate])
        except:
            answer.append([idx, 0.0])
        
    answer = sorted(answer, key=lambda x : (x[1]), reverse=True)
    result = [idx[0] for idx in answer]
    
    return result