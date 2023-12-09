S = 'K1KA5CB7'
# S = 'AJKDLSI412K4JSJ9D'

S = sorted(S)

answer, sum = '', 0
for s in S:
    try:
        sum += int(s)
    except:
        answer+=s
        
print(answer+str(sum))