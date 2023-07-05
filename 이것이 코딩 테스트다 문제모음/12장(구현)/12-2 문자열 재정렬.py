#S = 'K1KA5CB7' # 1 <= S <= 10,000
S = 'AJKDLSI412K4JSJ9D'

S = sorted(S)
number = ['0','1','2','3','4','5','6','7','8','9']
print(S)

numbers = 0
alphabets = ''
while(S):
            s = S.pop(0)
            if s in number:
                        numbers+=int(s)
            else:
                        alphabets+=s

print(alphabets+str(numbers))