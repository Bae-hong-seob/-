def solution(array, commands):
    answer = []
    for i in commands:
        start, end, k = i
        x = array[start-1:end]
        x.sort()
        answer.append(x[k-1])
    return answer