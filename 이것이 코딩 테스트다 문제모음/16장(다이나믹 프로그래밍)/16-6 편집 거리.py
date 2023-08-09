A = 'cat' # 1 <= len(A) <= 5000
B = 'cut'

# # A = 'sunday'
# # B = 'saturday'

# A = 'sundaykkk'
# B = 'sunday'

# solution
count = 0

while(len(A) != len(B)): # 길이는 맞춰야지
    if len(A) < len(B): # 삽입진행
        for idx in range(len(B)):
            if A[idx] != B[idx]: # 올바른 위치에 삽입하는게 이득
                A = A[:idx] + B[idx] + A[idx:]
                count+=1
                break
    elif len(A) > len(B): # 삭제진행
        for idx in range(len(A)):
            try:
                if A[idx] != B[idx]: # 안맞는거 일단 삭제
                    A = A[:idx] + A[idx+1:]
                    count+=1
                    break
            except:
                A = A[:idx] + A[idx+1:]
                count+=1
                break
        
# 길이는 맞췄으니 교체 진행
for idx in range(len(A)):
    if A[idx] != B[idx]: # 교체하자
        A = A.replace(A[idx], B[idx])
        count+=1

print(A,B)
print(count)