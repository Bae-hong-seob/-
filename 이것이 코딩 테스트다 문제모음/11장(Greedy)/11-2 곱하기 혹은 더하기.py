N = '01010011'

N_list = list(map(int,N))

answer=0
for num in N_list:
    if num==0 or num==1 or answer==0:
        answer+=num
    else:
        answer*=num

print(answer)