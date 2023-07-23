array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print('before : ', array)

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    
    while left <= right: # 엇갈렸다면 피벗을 가운데 위치시키고 반복문 종료.
        
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]: # pivot 값보다 작으면 오른쪽 끝까지 탐색(큰 수를 탐색)
            left+=1
            
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]: # pivot 값보다 크면 왼쪽 끝까지 탐색(작은 수를 탐색)
            right-=1
            
        if left > right: # 엇갈렸다면 작은 right-=1 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left] , array[right] = array[right], array[left]
            
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
    
quick_sort(array, 0, len(array)-1)
print('after : ', array)