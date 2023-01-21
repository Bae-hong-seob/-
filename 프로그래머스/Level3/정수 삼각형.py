def solution(triangle):
    sum_list = [triangle[0]]
    print(type(triangle[0][0]))
    for i in range(1,len(triangle)):
        row = []
        for j in range(len(triangle[i])):
            if j==0: #left leaf
                row.append(sum_list[i-1][j] + triangle[i][j])
            elif j==len(triangle[i])-1: #right leaf
                row.append(sum_list[i-1][j-1] + triangle[i][j])
            else: #mid leaf
                row.append(max(sum_list[i-1][j-1], sum_list[i-1][j]) + triangle[i][j])
        sum_list.append(row)

    return max(sum_list[-1])