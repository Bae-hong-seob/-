def solution(n):
    answer = ''
    while n>0:
        n-=1
        last = n%3
        if last == 0:
            last = '1'
        elif last == 1:
            last='2'
        elif last==2:
            last='4'
        n = n//3
        answer = str(last)+answer
    
    return answer