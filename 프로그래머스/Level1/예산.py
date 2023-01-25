def solution(d, budget):
    count = 0
    d.sort(reverse=True)
    while(d):
        cost = d.pop()
        if budget < cost:
            break
        else:
            budget-=cost
            count+=1
        
    return count