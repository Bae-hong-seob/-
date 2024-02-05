from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    
    while(prices):
        price = prices.popleft()
        count=0
        for i in prices:
            if i >= price:
                count+=1
            else:
                count+=1
                break
        answer.append(count)
                
    return answer