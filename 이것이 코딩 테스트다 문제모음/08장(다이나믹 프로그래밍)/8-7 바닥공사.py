# N = 3 # 1 <= N <= 1000

# import math 

# if N % 2 == 0: #2로 나누어 떨어지는 경우
#     number_of_tiles = (N // 2)
# else:
#     number_of_tiles = (N // 2) + 1
    
# print(number_of_tiles)
    
# answer = math.factorial(number_of_tiles)
# answer = answer*3*(N//2)
# print(answer%796796)

# solution
n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1]+ d[i-2]*2) % 796796
    
print(d[n])