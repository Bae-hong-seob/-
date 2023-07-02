n,m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
            # 각 무게에 해당하는 볼링공의 개수 카운트
            array[x] += 1
            
result = 0
# 1부터 m까지의 각 무게에 대하여 처리. 단 무게가 무거워질수록 이전 경우의 수는 제거해주어야함.
for i in range(1, m+1):
            n -= array[i] # 무게가 i인 볼링공의 개수 제외(A가 선택할 수 있는 개수)
            result += array[i] * n  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) * 무게가 i가 아닌 볼링공의 개수(B가 선택할 수 있는 개수)
            
print(result)