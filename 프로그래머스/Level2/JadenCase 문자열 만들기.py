def solution(s):
    #s = " adg   3eagdag   "
    s_list = s.split(" ")
    print(s_list)
    answer = ''
            
    for word in s_list:
        if word == '':
            answer += ' '
            continue
        word = word[0].upper() + word[1:].lower()
        answer += (word + ' ')

    return answer[:-1]

# def solution(s):
#     s = s.split(" ")
#     for i in range(len(s)):
#         s[i] = s[i][:1].upper() + s[i][1:].lower()
#     return ' '.join(s)