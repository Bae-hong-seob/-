N = '123402'

mid = (0+len(N))//2
left, right = N[:mid], N[mid:]
print(left, right)

left_sum, right_sum = 0,0
for i,j in zip(left, right):
    left_sum+=int(i)
    right_sum+=int(j)

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')