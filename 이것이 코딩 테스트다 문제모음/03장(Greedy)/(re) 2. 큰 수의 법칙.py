N, M, K = 5,8,3
number_list = [2,4,5,4,6]

number_list.sort()

first = number_list[-1]
second = number_list[-2]

answer = (first*K + second) * (M//(K+1)) + (first*(M%(K+1)))
print(answer)