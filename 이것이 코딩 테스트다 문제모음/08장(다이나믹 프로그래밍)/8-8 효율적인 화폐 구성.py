N,M = 2,15 # 1 <= N <= 100, 1 <= M <= 10000
dollars = [2,3]

# N,M = 3,4
# dollars = [3,5,7]

dollars.sort(reverse=True)
count = 0

for dollar in dollars:
    if M ==0: # 다 거슬러줬을 때
        break
    
    if dollar > M: # 해당 화폐로는 거슬러줄 수 없으면
        continue
    
    elif dollar <= M: # 해당 화폐로 거슬러 줄 때
        count += M // dollar
        M-=(count * dollar)
        
if M == 0:
    print(count)
else:
    print(-1)
    
# solution
n,m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
    
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001: # i-k 원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])