from itertools import combinations

N,M = 8,5
weight_list = [1, 5, 4, 3, 2, 4, 5, 2]

# solution
weight_list = list(combinations(weight_list,2))
count=len(weight_list)
for check in weight_list:
            if check[0] == check[1]: # 무게가 같은 경우는 배제
                        count-=1
                        
print(count)