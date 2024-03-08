# 알아야할 수학 개념

1. 소수인지 확인하는 방법(1은 소수가 아니다) - x의 제곱근까지의 수만 확인하면 됨.
~~~
# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
~~~
2. 10진법 -> k진법 변환
~~~
k_n = ''
while n>0: #k진수 변환.
    n, last = n//k, n%k
    k_n = str(last) + k_n
~~~
3. 

# 함수별 시간복잡도
len() : O(1)
