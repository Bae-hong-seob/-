def solution(s):
    num_change = 0
    num_zero = 0
    while(s != '1'):
        num_zero += s.count('0')
        s = s.replace('0','')
        
        num10 = len(s)
        s = str(format(num10, 'b'))
        num_change += 1

    answer = [num_change, num_zero]
    return answer