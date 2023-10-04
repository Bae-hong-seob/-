N = 5

count = 0
for hour in range(N+1):
    for minute in range(60):
        for second in range(60):
            if any(['3' in str(hour), '3' in str(minute), '3' in str(second)]):
                count+=1

print(count)