from collections import Counter, defaultdict, deque

def solution(gems):
    counter = Counter(gems)
    number_of_types = len(counter.keys())
    now_gems_dq = deque([])
    now_gems_dict = defaultdict(int)
    answer, length = [], int(1e9)
    for idx,gem in enumerate(gems): #최대 100,000
        #print(idx, gem, now_gems_dq, now_gems_dict)
        while now_gems_dq and now_gems_dict[now_gems_dq[0][0]]>1: #왼쪽 같은거 여러개일시 포인터 오른쪽으로 이동
            now_gems_dict[now_gems_dq[0][0]]-=1
            now_gems_dq.popleft()
            
        if len(now_gems_dict.keys()) == number_of_types:
            if len(now_gems_dq) < length: #최소 길이 발견
                answer, length = [now_gems_dq[0][1]+1, now_gems_dq[-1][1]+1], len(now_gems_dq)
                
            g, i = now_gems_dq.popleft() #왼쪽 포인터 오른쪽으로 한칸 이동
            del now_gems_dict[g]

            
        now_gems_dq.append([gem,idx]) #오른쪽 포인터 이동
        now_gems_dict[gem]+=1 
    
    #오른쪽 포인터는 모두 이동. 왼쪽을 줄일수만 있음.
    while now_gems_dq and now_gems_dict[now_gems_dq[0][0]]>1: #왼쪽 같은거 여러개일시 포인터 오른쪽으로 이동
        now_gems_dict[now_gems_dq[0][0]]-=1
        now_gems_dq.popleft()
    
    if len(now_gems_dict.keys()) == number_of_types and len(now_gems_dq) < length: #최소 길이 발견
        answer, length = [now_gems_dq[0][1]+1, now_gems_dq[-1][1]+1], len(now_gems_dq)
    
    return answer