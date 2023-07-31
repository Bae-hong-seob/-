N = 5 # 1 <= N <= 1000000
numbers = [-15, -6, 1, 3, 7] # -10e9 <= 원소 <= 10e9

# N = 7
# numbers = [-15, -4, 2, 8, 9, 13, 15]

answers = []

def binary_search(array, start, end):
    if start > end:
        return None
    
    mid  = (start + end) //2
    
    if mid == array[mid]: # 고정점 확인
        return answers.append(mid)
    
    elif mid > array[mid]: # index가 더 큰 경우 오른쪽으로 탐색 진행
        return binary_search(array, mid+1, end)
    
    else: # index가 더 작은 경우 왼쪽으로 탐색 진행
        return binary_search(array, start, mid-1)
    
binary_search(numbers, 0, len(numbers)-1)
    
if len(answers) == 0:
    print(-1)
else:
    print(answers)