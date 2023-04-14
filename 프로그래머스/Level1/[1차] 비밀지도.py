def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    
    for i in arr1:
        row = str(format(i,'b'))
        if len(row) != n:
            row = '0'*(n - len(row)) + row
        map1.append(row)
        
    for i in arr2:
        row = str(format(i,'b'))
        if len(row) != n:
            row = '0'*(n - len(row)) + row
        map2.append(row)
    
    answer = []
    for i,j in zip(map1, map2):
        row = ''
        for k in range(n):
            if i[k] == '0' and j[k] == '0': # 둘 다 공백일때
                row+=' '
            else:
                row+='#'
        answer.append(row)
            
    return answer