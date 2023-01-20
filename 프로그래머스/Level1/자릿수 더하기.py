# def solution(n):
#     answer=0
    
#     for i in range(1,len(str(n))+1):
#         answer+= (n%10)
#         n = n//10
    
#     return answer
def solution(n):    
    return sum([int(i) for i in str(n)])