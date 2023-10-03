N,M = 5,3
weight_list = [1,3,2,3,2]

N,M = 8,5
weight_list = [1, 5, 4, 3, 2, 4, 5, 2]

from itertools import combinations

answer = 0
for a,b in list(combinations(weight_list,2)):
    if a != b:
        answer+=1
        
print(answer)