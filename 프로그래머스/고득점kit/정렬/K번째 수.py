def solution(array, commands):
    answer = []

    for i,j,k in commands:
        candidate = array[i-1:j]
        candidate.sort()
        answer.append(candidate[k-1])
        
    return answer