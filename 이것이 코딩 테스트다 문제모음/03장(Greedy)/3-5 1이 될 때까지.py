import time

N, K = 25,5 # 항상 N >= K, 2 <= N < = 100,000 , 2 <= K <= 100,000

# solution
answer = 0

start_time = time.time()
while(N > 1):
            if N % K ==0: #나누어질 때
                        N = N // K
                        answer+=1
            else:
                        N -= 1
                        answer+=1
end_time = time.time()
print(end_time - start_time)

print(answer)