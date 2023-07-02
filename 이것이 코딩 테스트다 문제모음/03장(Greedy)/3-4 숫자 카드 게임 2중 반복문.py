N1, M1 = 3,3
matrix1 = [[3,1,2], [4,1,4], [2,2,2]]

N2, M2 = 2,4
matrix2 = [[7,3,1,8], [3,3,3,4]]

# solution
answer_list = []
for row in matrix2:
            min_value = 10001 # 각 숫자는 1이상 10,000이하
            for num in row:
                        min_value = min(min_value, num)
            answer_list.append(min_value)
            
answer = max(answer_list)
print(answer)