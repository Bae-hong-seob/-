N = '123402'
N = '7755'
N = input()

mid = len(N)//2
if sum([int(i) for i in N[:mid]]) == sum([int(i) for i in N[mid:]]):
    print('LUCKY')
else:
    print("READY")