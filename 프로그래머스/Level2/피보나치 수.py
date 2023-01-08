def solution(n):
    list = [0,1]
    for i in range(2,n+1):
        list.append(list[i-1]+list[i-2])
    answer = list[-1] % 1234567
    return answer

# def solution(n):
#     def fibonacci(n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         return fibonacci(n-1) + fibonacci(n-2)
    
#     num = fibonacci(n)
#     answer = num % 1234567
#     return answer