# S = 'K1KA5CB7'
S = 'AJKDLSI412K4JSJ9D'

S = sorted(S)

numbers, alphabets = [],[]
for s in S:
    try:
        numbers.append(int(s))
    except:
        alphabets.append(s)

alphabets.append(str(sum(numbers)))
print(''.join(alphabets))