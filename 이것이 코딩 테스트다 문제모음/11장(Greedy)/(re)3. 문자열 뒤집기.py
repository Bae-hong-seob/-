S = '0001100'

idx, zero, one = 0,0,0
for _ in range(len(S)):
    if idx >= len(S):
        break
    value = S[idx]
    
    while True:
        idx+=1 # next str
        if idx >= len(S): # 끝까지 탐색한 경우
            break
        
        if value != S[idx]: # 다르면 스탑
            break

    
    if value == '0':
        zero+=1
    else:
        one+=1

print(zero,one)
print(min(zero, one)) # 연속된 숫자 무리 중에 작은거 출력