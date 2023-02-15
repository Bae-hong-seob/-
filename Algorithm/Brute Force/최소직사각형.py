def solution(sizes):
    a = [max(i) for i in sizes]
    b = [min(i) for i in sizes]
    return max(a)*max(b)