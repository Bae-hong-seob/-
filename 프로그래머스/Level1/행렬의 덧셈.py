# def solution(arr1, arr2):
#     answer = []
    
#     for first, second in zip(arr1, arr2):
#         row = []
#         for value1, value2 in zip(first, second):
#             row.append(value1+value2)
#         answer.append(row)
#     return answer

def solution(A, B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer