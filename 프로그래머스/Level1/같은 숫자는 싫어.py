# def solution(arr): #arr의 원소가 0~9까지 숫자일때만 가능. 
#     arr.append(99) #index range를 위해 아닌 수 하나 추가
#     return [arr[i] for i in range(len(arr)-1) if arr[i]!=arr[i+1]]

def solution(s): #배열의 원소가 뭐든 반복적인 것은 삭제하는 코드.
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a