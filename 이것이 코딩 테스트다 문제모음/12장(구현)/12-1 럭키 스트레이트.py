# 럭키 스트레이트를 사용할 수 있으면 'LUCKY', 사용할 수 없으면 'READY' 출력
N = 7755 # # 10 <= N <= 99,999,999. 단 자릿수는 항상 짝수로만 주어짐. 반으로 나눌 수 있게

length = len(str(N))
N_list = list(str(N))

first = [int(n) for index,n in enumerate(N_list) if index < length//2]
second = [int(n) for index,n in enumerate(N_list) if index >= length//2]
print(first)
print(second)

if sum(first) == sum(second):
            print('LUCKY')
else:
            print('READY')