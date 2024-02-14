def solution(number, k): # 이게 훨씬 빠름
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

def solution(number, k):
    stack = []
    n = len(number)
    for idx, num in enumerate(number):
        #print(stack, num, number[idx+1:])
        if idx==0:
            stack.append(num)
            continue

        while stack and stack[-1] < num and len(number[idx+1:]) >= n-k-len(stack):
            stack.pop()
            
        if len(stack) < n-k:
            stack.append(num)
    #print(stack)
    return ''.join(stack)