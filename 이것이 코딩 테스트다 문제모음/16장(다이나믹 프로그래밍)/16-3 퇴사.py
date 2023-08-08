N = 7 # 1 <= N <= 15
schedule = [ # 1 <= T <= 5 , 1 <= P <= 1000
    [3,10],
    [5,20],
    [1,10],
    [1,20],
    [2,15],
    [4,40],
    [2,200]
]

dp_table = [0 for _ in range(N+5)] 
 
for idx in range(N):
    for how_long, cost in schedule[:idx]:
        print('idx, how_long : ', idx, how_long)
        if idx - how_long >= 0:
            dp_table[idx] = max(dp_table[idx], dp_table[idx-1] + schedule[idx-how_long][1])
            print(idx, how_long, dp_table)
        
    # dp_table[idx + how_long] = max(dp_table[idx+how_long] + cost, schedule[idx][1])
    #print(n, dp_table)
    
print(dp_table[:N])