from collections import defaultdict, deque
from itertools import combinations, combinations_with_replacement, permutations, product

def solution(user_id, banned_id):
    user2ban, banNumberDict = defaultdict(set), defaultdict(int)
    for b in banned_id:
        banNumberDict[b]+=1
        
    for b in banned_id: # 최대 8번
        for u in user_id: #최대 8번
            if len(b) != len(u):
                continue
                
            banned = True
            for bc, uc in zip(b,u): #최대 8번 -> 8*8*8. 최대 512번.
                if bc=='*':
                    continue
                
                if bc!=uc:
                    banned=False
                    break
                    
            if banned:
                user2ban[u].add(b)
    #print(user2ban)
    #print(banNumberDict)
    
    answer = set()
    for candidates in permutations(user_id, len(banned_id)): # 최대 8C3 * 3! = 8*7*6 = 336번.
        numberdict = banNumberDict.copy()
        
        available = True
        
        for candidate in candidates: # 최대 8번 -> 336*8번 = 대충 2600번
            ban_ids = user2ban[candidate]
            if not ban_ids:
                available=False
                break
            
            loop=True
            for ban_id in ban_ids:
                if numberdict[ban_id]>0:
                    numberdict[ban_id]-=1
                    loop=False
                    break

            if loop: #ban_ids를 다 돌아봐도 가능한게 없다
                available=False
                break
                    
        #print(candidates, type(candidates), numberdict, available)
        if available:
            answer.add(tuple(sorted(candidates)))
    #print(answer)
    return len(answer)