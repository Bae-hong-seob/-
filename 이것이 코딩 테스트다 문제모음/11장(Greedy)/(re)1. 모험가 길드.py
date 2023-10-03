N = 5
scared = [2,3,1,2,2]

scared.sort()

print(scared)

answer = 0
while scared:
    number_of_gruop = scared[-1]
    try: # 그룹 결성이 가능한 경우
        for i in range(number_of_gruop):
            scared.pop()
        answer+=1
    except: # 그룹 결성이 불가능한 경우
        break
    
print(answer)    