def solution(citations):
    citations.sort()
    for idx , citation in enumerate(citations): #enumerate 는 list의 index와 value를 반환.
        print(idx, citation, citations)
        if citation >= len(citations) - idx :
            return len(citations) - idx
    return 0