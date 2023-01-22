def solution(n, s):
    answer = [int(s/n) for i in range(n)]
    if n>s:
        return [-1]

    for i in range(s%n):
        answer[i]+=1
    return sorted(answer)
