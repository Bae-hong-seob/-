# import math

# def solution(n):
#     sqrt_n = math.sqrt(n)
#     int_n = int(sqrt_n)
    
#     if math.pow(int_n,2) == float(n):
#         return int(math.pow(sqrt_n+1,2))
#     else:
#         return -1
def solution(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    else:
        return -1