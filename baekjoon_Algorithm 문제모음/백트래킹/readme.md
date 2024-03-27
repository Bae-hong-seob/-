from itertools import permutations

N,M = 3,1
N,M = 4,2
N,M = 4,4
N,M = map(int, input().split())
for candidates in permutations([i for i in range(1,N+1)],M):
    for candidate in candidates:
        print(candidate, end=' ')
    print()
