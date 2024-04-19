N,x = 7,2
numbers = [1,1,2,2,2,2,3]

N,x = 7,4
numbers = [1,1,2,2,2,2,3]

pivot = N//2
left,right = 0,N-1

available=True

# 이진탐색을 통해 원하는 값 탐색
while numbers[pivot]!=x:
    if left==right:
        available=False
        break
    
    if pivot>x:
        left=pivot+1
        pivot = (left+right)//2
        
    else:
        right = pivot-1
        pivot = (left+right)//2

count=0
# 원하는 값에서 왼쪽으로 탐색 진행
for left in range(pivot,-1,-1):
    if numbers[left]==x:
        count+=1
    else:
        break

for right in range(pivot+1,N):
    if numbers[right]==x:
        count+=1
    else:
        break
    
if available:
    print(count)
else:
    print(-1)