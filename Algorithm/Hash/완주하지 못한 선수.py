def solution(participant, completion):
    participants = {}
    completions = {}
    for i in participant:
        try:
            participants[i] += 1
        except:
            participants[i] = 1
    
    for i in completion:
        try:
            completions[i] += 1
        except:
            completions[i] = 1
    
    answer = [i for i in participants if i not in completions or participants[i]!=completions[i]]
    return ''.join(answer)