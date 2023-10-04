N, K = 25,5

# 계속 1씩 빼는게 아니라 배수가 될 때를 target으로 한번에 빼버릴 수도 있잖아?
count=0
while N != 1:
    if N % K == 0:
        N/=K
        count+=1
    else:
        target = (N//K) * K
        count+=N-target
        N = target
        
print(count)