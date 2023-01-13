def solution(price, money, count):
    for i in range(count):
        money -= price*(i+1)
        
    if money < 0:
        answer = -1 * money
    else:
        answer = 0

    return answer