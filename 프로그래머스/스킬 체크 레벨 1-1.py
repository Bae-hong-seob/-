def solution(n):
    x = [int(a) for a in str(n)]
    x.sort(reverse=True)
    print(x)

    ordered_num = ''

    for i in x:
        i = str(i)
        ordered_num += i

    print(ordered_num)
    answer = int(ordered_num)
    return answer