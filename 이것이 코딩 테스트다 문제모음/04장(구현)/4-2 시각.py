N = 5 # 0<= N <= 23

#첫번째 자리 수
hours = [str(i) for i in range(N+1)]
minutes = [str(i) for i in range(60)]
seconds = [str(i) for i in range(60)]

candidates = []

for hour in hours:
            for minute in minutes:
                        for second in seconds:
                                    candidates.append(hour+minute+second)
print(len(candidates))
answer = 0
                                    
for candidate in candidates:
            if '3' in candidate:
                        answer+=1
                        
print(answer)