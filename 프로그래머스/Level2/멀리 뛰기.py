def solution(n):
    
    fibonacci = [1,1]
    for i in range(2, n+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    return fibonacci[n] % 1234567