data = input()
count0 = 0
count1 = 0

if data[0] == '1':
            count0+=1
else:
            count1+=1
            
for i in range(len(data)-1):
            if data[i] != data[i+1]: #연속되지 않은 경우
                                    if data[i+1] == '1':
                                                count0+=1
                                    else:
                                                count1+=1
                                                
print(min(count0,count1))