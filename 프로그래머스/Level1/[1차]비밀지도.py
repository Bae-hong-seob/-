def solution(n, arr1, arr2):
    n = len(arr1)
    map1, map2 = [], []
    for number1,number2 in zip(arr1, arr2):
        number1, number2 = str(format(number1, 'b')), str(format(number2, 'b'))
        if len(number1) < n:
            number1 = '0'*(n-len(number1)) + number1
        if len(number2) < n:
            number2 = '0'*(n-len(number2)) + number2
        map1.append([int(i) for i in number1])
        map2.append([int(i) for i in number2])
    
    answers = []
    for number1, number2 in zip(map1, map2):
        answer = ''
        for i in range(n):
            if number1[i]==0 and number2[i]==0: #둘다 공백인 경우
                answer+=' '
            else:
                answer+='#'
        answers.append(answer)
    return answers