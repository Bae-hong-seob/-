N,M,K = 5,8,3 # 항상 K <= M
num_list = [2,4,5,4,6]

# # solution 1 -> 시간초과 가능성 있음
# answer = 0
# num_list = sorted(num_list)

# biggest = num_list[-1]
# second = num_list[-2]

# while(M > 0):
#             for _ in range(K):
#                         answer+=biggest
#                         M-=1
#             answer+=second
#             M-=1
# print(answer)

# solution 2 -> 규칙이 없을까 생각
answer = 0
num_list = sorted(num_list)

biggest = num_list[-1]
second = num_list[-2]

answer += ((biggest*K) + second) * (M // (K+1))
answer += (M % (K+1)) * biggest

print(answer)