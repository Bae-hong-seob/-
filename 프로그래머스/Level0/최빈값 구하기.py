def solution(array):
    answer = {}
    for i in array:
        answer[i] = array.count(i)
        
    answer = sorted(answer.items(), key = lambda item: item[1])
    
    try:
        num1, count1 = answer.pop()
        num2, count2 = answer.pop()
        if count1==count2:
            return -1
        else:
            return num1
    except:
        return num1