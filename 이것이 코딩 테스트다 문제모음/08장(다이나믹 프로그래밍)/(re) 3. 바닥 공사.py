N = 3

dp_table = [0]*(N+1)
dp_table[1], dp_table[2] = 1,3

for i in range(3,N+1):
    dp_table[i] = (dp_table[i-1] + dp_table[i-2]*2) % 796796

print(dp_table[-1])