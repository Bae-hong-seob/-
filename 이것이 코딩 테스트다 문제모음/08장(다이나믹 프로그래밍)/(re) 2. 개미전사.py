N = 4
stores = [1,3,1,5]

dp_table = [0]*N
dp_table[0], dp_table[1] = stores[0], stores[1]

for i in range(2,N):
    dp_table[i] = max(dp_table[i-2]+stores[i], dp_table[i-1])
    
print(dp_table)
print(dp_table[-1])