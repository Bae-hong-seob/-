def solution(n):
    answer = n
    binary_n = format(n, 'b')
    binary_answer = ''
    
    while(binary_answer.count('1') != binary_n.count('1')):
        answer+=1
        binary_answer = format(answer,'b')
    return answer