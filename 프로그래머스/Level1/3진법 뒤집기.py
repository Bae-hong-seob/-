# def solution(n):
#     three = []
#     while(n>=3):
#         three.append(n%3)
#         n= n//3
#     three.append(n)
    
#     answer=0
#     i=0
#     for num in reversed (three):
#         answer+=num*(3**i)
#         i+=1

#     return answer
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer