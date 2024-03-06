def k_number(number,k):
    if number == 0:
        return '0'
    
    k_num = ''
    last_char = ['A','B','C','D','E','F'] #최대 16진수
    while number>0:
        number, last = number//k, number%k
        if last >= 10: #나머지가 10이상인 경우는 10이상 진법인 경우.
            last = last_char[last-10]
        k_num = str(last)+k_num
    return k_num

def solution(n, t, m, p):
    n_numbers = [] #최대 1000개 저장
    for number in range(t*m): #최대 100,000 번.
        n_number = k_number(number,n)
        n_numbers.extend([i for i in n_number])
    
    answer, i = '',0
    for tube in range(p-1, len(n_numbers), m):
        answer+=n_numbers[tube]
        i+=1
        if i == t:
            break
    
    return answer