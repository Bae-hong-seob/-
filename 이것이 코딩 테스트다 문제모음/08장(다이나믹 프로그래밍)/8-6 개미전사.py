N = 4 # 3 <= N <= 100
stores = [1,3,1,5] # 0 <= K <= 1000

answer = 0
idx=0

while idx < len(stores):
    tmp_answer1 = answer+stores[idx]
    tmp_answer2 = answer+stores[idx+1]
    
    print(tmp_answer1, tmp_answer2)
    
    if tmp_answer1 >= tmp_answer2:
        answer = tmp_answer1
        idx+=1
    elif tmp_answer1 < tmp_answer2:
        answer = tmp_answer2
        idx+=2
    
print(answer)