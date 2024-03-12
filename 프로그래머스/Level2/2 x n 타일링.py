def solution(n):
    dp_table = [0]*(n+1) #index가 가로길이(n)
    dp_table[1] = 1
    dp_table[2] = 2
    
    
    for i in range(3,n+1): #최대 60,000번. 피보나치 수열 n=60,000일때 f(n) = 8억. 나누는 수는 10억.
        dp_table[i] = (dp_table[i-1] + dp_table[i-2])% 1000000007
    
    return dp_table[n] #마지막 나머지 연산 실행 시 시간초과 발생