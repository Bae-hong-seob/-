import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(n, k):
    k_n = ''
    while n>0: #k진수 변환.
        n, last = n//k, n%k
        k_n = str(last) + k_n
        
    answer = 0
    for number in k_n.split('0'):
        try:
            number = int(number)
            if number == 1: #1은 소수가 아님
                continue

            if is_prime_number(number):
                answer+=1
        except:
            continue
    return answer