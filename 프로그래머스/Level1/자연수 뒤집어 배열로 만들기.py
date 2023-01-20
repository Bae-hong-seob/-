# def solution(n):
#     n = [int(i) for i in str(n)]
#     answer = []
#     for i in range(len(n)):
#         answer.append(n.pop())
#     return answer
def solution(n):
    return list(int(i) for i in reversed(str(n)))