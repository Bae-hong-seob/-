from itertools import combinations 

N = 5
N_list = [1,1,1,1,1]

possible_list = []
for i in range(1,N+1):
            possible = list(map(sum,set(combinations(N_list,i))))
            possible_list.extend(possible)
possible_list = sorted(set(possible_list))

for i in range(1,sum(N_list)+1):
            if i not in possible_list:
                        answer = i
                        break
try:
            print(answer)
except:
            print(max(possible_list)+1)