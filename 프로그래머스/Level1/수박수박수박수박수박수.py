# def solution(n):
#     answer = ''
#     for idx in range(n):
#         if idx%2==0:
#             answer+='수'
#         else:
#             answer+='박'
#     return answer
def solution(n):
    return "수박"*(n//2) + "수"*(n%2)