import time

N, K = 25,5 # 항상 N >= K, 2 <= N < = 100,000 , 2 <= K <= 100,000

# solution
answer = 0

start_time = time.time()
while(N > 1):
            target = (N // K) * K
            answer += N - target # 목표 값까지 1을 한번에 빼기.
            N = target # 배수로 변경
            
            if N < K: 
                        break
            N /= K # 배수로 만들었으니 가능
            answer+=1

answer += N-1 # N이 K보다 작은채로 남았다면 1이 될때까지 빼야함.
end_time = time.time()
print(end_time - start_time)

print(answer)