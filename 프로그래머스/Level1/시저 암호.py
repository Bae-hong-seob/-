def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if i >= 'A' and i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer

# def solution(s, n):
#     answer=''
    
#     for i in s:
#         if i == ' ':
#             answer+=' '
#         elif ord(i)>=97 and ord(i)<=122: #소문자
#             if ord(i)+n > 122:
#                 answer+=chr(96 + abs(122 - (ord(i)+n)))
#             else:
#                 answer+=chr(ord(i)+n)
#         else: # 대문자
#             if ord(i)+n > 90:
#                 answer+=chr(64 + abs(90 - (ord(i)+n)))
#             else:
#                 answer+=chr(ord(i)+n)
    
#     return answer