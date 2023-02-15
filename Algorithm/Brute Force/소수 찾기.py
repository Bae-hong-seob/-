def solution(n):
    answer = []
    for i in range(1,n+1,2): #짝수는 소수일수가 없다
        count = 0
        for j in range(1,int(i**(1/2))+1):
            if i%j == 0:
                count+=1
            if count>1:
                break
        answer.append(count)
    return answer.count(1)+1-1 #2추가 #1제거