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
    target_length = len(number)-k
    
    for idx, num in enumerate(number):
        if len(stack)==0:
            stack.append(num)
            continue
            
        if len(number[idx:]) > target_length-len(stack) and num > stack[-1]: # 교체
            for _ in range(len(stack)):
                if len(number[idx:]) > target_length-len(stack) and num > stack[-1]:
                    stack.pop()
                else:
                    break
            stack.append(num)
        else:
            if len(stack) < target_length:
                stack.append(num)
        
    answer = ''
    return ''.join(stack)