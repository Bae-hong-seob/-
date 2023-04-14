def solution(a, b, n):
    answer = 0

    while(n>=a):
        answer += (n//a)*b # 몫 개수만큼 콜라 새로 받기
        
        n = n - (n//a)*a + (n//a)*b # 빈병 - 반납개수 + 새로받은 개수
        
    return answer