from collections import deque

def make_set(str1):
    set1 = []
    dq = deque()

    for char in str1: #최대 1,000번
        if char.isalpha() == False: #알파벳이 아닌 경우는 무시.
            if dq and len(dq)==2:
                set1.append(''.join(list(dq)))
            dq = deque()
            continue
        elif len(dq) < 2: #알파벳이고 dq의 길이가 2이하 일때는 추가.
            dq.append(char)
            continue
        else:
            set1.append(''.join(list(dq)))
            dq.popleft()
            dq.append(char)
            
    if dq:
        set1.append(''.join(list(dq)))
    return set1
    
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    set1, set2 = make_set(str1), make_set(str2)
    if len(set1) + len(set2) == 0: #둘다 공집합인 경우
        return 65536
    
    min_set = set1 if len(set1) <= len(set2) else set2
    max_set = set2 if len(set1) <= len(set2) else set1
    min_value = len(min_set)
    
    union, difference = [],[]
    for char in min_set: #최대 1,000 -1번 반복.
        if char in max_set: #교집합
            union.append(char)
            max_set.remove(char)
        else:
            difference.append(char)
    
    '''
    union : AUB
    difference : A-B
    max_set: B-A
    '''
    
    return int((len(union) / (len(union) + len(difference) + len(max_set)))*65536)