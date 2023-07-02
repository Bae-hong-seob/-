N1, M1 = 3,3
matrix1 = [[3,1,2], [4,1,4], [2,2,2]]

N2, M2 = 2,4
matrix2 = [[7,3,1,8], [3,3,3,4]]

# solution1
answer_list = []
for row in matrix1:
            answer_list.append(min(row))
            
answer = max(answer_list)
print(answer)