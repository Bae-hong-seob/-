S = '567'

answer = 0
for s in S:
    if answer == 0: # 
        answer+=int(s)
        continue
        
    if s == '0' or s == '1':
        answer+=int(s)
    else:
        answer*=int(s)
        
print(answer)