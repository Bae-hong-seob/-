def solution(sizes):
    w = max([max(size) for size in sizes])
    h = max([min(size) for size in sizes])
    return w*h