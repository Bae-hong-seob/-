def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for num in arr[1:]:
        if num == answer[-1]:
            continue
        else:
            answer.append(num)
    return answer