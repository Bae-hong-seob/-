data = input()

result = int(data[0])

for i in range(1, len(data)):
            # result, data[i] 중 하나라도 0,1인 경우 더하기 수행
            num = int(data[i])
            if num <= 1 or result <= 1:
                        result+=num
            else:
                        result*=num
print(result)