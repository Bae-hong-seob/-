def solution(n, left, right):
    '''
    [1,2,3, ... , n]
    [2,2,3, ... , n]
    ...
    [n,n,n, ... , n]
    '''
    left_share, left_last = left//n, left%n
    right_share, right_last = right//n, right%n
    # print(left_share, left_last)
    # print(right_share, right_last)
    
    answer = []
    if left_share < right_share: #시작 row와 끝 row가 다른 경우
        for i in range(left_share, right_share+1):
            now = [i+1]*(i+1) + [j for j in range(i+2, n+1)]
            if i == left_share:
                answer.extend(now[left_last:])
            elif i == right_share:
                answer.extend(now[:right_last+1])
            else:
                answer.extend(now)
    else: #같은 row에서 시작과 끝이 발생할 경우.
        now = [left_share+1]*(left_share+1) + [j for j in range(left_share+2, n+1)]
        answer.extend(now[left_last:right_last+1])
                
        
    return answer

def solution(n, left, right):
    result = []
    
    for i in range(left, right+1):
        # left ~ right 사이의 숫자를 n으로 나누면
        # 몫은 y(index) 좌표를
        # 나머지는 x(index) 좌표를 알 수 있다.
        y, x = i//n, i%n
        
        # 넣을 값은 (y,x 좌표중 큰 값) + 1
        # [0][0]=1 [0][1]=2 [0][2]=3 [0][3]=4
        # [1][0]=2 [1][1]=2 [1][2]=3 [1][3]=4
        # [2][0]=3 [2][1]=3 [2][2]=3 [2][3]=4
        # [3][0]=4 [3][1]=4 [3][2]=4 [3][3]=4
        value = max(y,x) + 1
        
        result.append(value)
        
    return result