def solution(number):
    answer = 0
    
    for i in range(len(number)):
        first = number[i]
        try:
            for j in range(i+1,len(number)):
                second = number[j]
                for k in range(j+1, len(number)):
                    third = number[k]
                    if first+second+third == 0:
                        answer+=1
        except:
            return answer
    return answer