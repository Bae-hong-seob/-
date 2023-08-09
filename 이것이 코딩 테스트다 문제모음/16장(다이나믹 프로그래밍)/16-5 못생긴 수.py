N = int(input()) # 1 <= N <= 1000

# N=10

# 2**a, 3**b, 5**c a+b+c <= 1000.
# 1,000,000,000 10억 연산 1초 불가능.
# 300 300 300 -> 27,000,000 가능.

answers = []
for a in range(N):
    for b in range(N-a):
        for c in range(N-a-b):
            answers.append(2**a * 3**b * 5**c)
            
answers.sort()
print(answers[N-1])