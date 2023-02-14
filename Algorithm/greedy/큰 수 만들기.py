def solution(number, k):
    box = []
    for i in number:
        if box == []: #stack이 비어있을 경우
            box.append(i)
        else:
            while box != [] and int(box[-1]) < int(i) and k > 0 : 
                box.pop()
                k-=1
            box.append(i)
            
    while k>0:
        box.pop()
        k-=1
    return ''.join(box)