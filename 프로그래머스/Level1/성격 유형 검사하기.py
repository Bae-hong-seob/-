def solution(survey, choices):
    mbti = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for query, answer in zip(survey, choices):
        if answer == 4:
            continue
            
        if query != ''.join(sorted(query)):
            query = ''.join(sorted(query))
            answer = 8-answer
        

        if answer < 4:
            mbti[query[0]] += (4-answer)
        else:
            mbti[query[1]] += (answer-4)
    
    answer = ''
    if mbti['R'] >= mbti['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if mbti['C'] >= mbti['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if mbti['J'] >= mbti['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if mbti['A'] >= mbti['N']:
        answer += 'A'
    else:
        answer += 'N'
                
    return answer