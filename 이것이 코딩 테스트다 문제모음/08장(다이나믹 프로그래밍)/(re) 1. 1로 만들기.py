X = 26

INF = 1e9
d = [INF]*(X+1)
d[0], d[1] = 0,0

for x in range(2,X+1):
    if x % 5 == 0:
        d[x] = min(d[x//5]+1, d[x])
        
    if x % 3 == 0:
        d[x] = min(d[x//3]+1, d[x])
    
    if x % 2 == 0:
        d[x] = min(d[x//2]+1, d[x])
    
    d[x] = min(d[x-1]+1, d[x])

print(d)
print(d[-1])