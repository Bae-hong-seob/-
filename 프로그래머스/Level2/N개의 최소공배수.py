def solution(arr):
    arr.sort()
    answer = arr[0]
    
    for i in range(1,len(arr)):
        a, b = answer, arr[i]
        
        max = a*b
        
        while(answer!=max):
            for j in range(1,(max//b)+1):
                for k in range(1,(max//a)+1):
                    if b*j == a*k:
                        answer = b*j
                        break
                if b*j == a*k:
                    break
            if b*j == a*k:
                break
        
    return answer