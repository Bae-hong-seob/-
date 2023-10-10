N,M = 2,15
coins = [2,3]

# N,M = 3,4
# coins = [3,5,7]

# N,M = 3,7
# coins = [2,3,5]

INF = 1e9
dp_table = [INF]*(10000+1)

for coin in coins:
    dp_table[coin] = 1

for i in range(1,M+1):
    for coin in coins:
        if i-coin >= 0:
            dp_table[i] = min(dp_table[i], dp_table[i-coin]+1)

if dp_table[M] == INF:
    print(dp_table[:M+1])
    print(-1)
else:
    print(dp_table[:M+1])
    print(dp_table[M])