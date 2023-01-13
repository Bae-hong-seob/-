def solution(strings, n):
    strings.sort()
    
    char_list = []
    answer = []

    for i in strings:
        char_list.append(i[n])
    char_list.sort()
    
    for j in char_list:
        for k in strings:
            if j == k[n] and k not in answer:
                answer.append(k)
                continue
    return answer