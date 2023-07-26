N = 5 # 가게의 부품 종류 1 <= N <= 1000000
stores = [8,3,7,9,2] # 각 원소는 1보다 크고 1000000이하

M = 3 # 손님이 요청한 부품 종류 1 <= M <= 1000000
customers = [5,7,9] # 각 원소는 1보다 크고 10억 이하.

# solution
stores.sort()
print(stores)

def binary_search(array, target, start, end):
    mid = (start + end) // 2
    
    if start > end: # 다 탐색한 경우임
        return 'no'
    
    if array[mid] == target:
        return 'yes'

    elif target < array[mid]: # 끝점을 왼쪽으로 이동
        return binary_search(array, target, start, mid-1)
        
    elif target > array[mid]: # 시작점을 오른쪽으로 이동
        return binary_search(array, target, mid+1, end)
    
    
answers = []
for customer in customers:
    answers.append(binary_search(stores, customer, 0, len(stores)-1))
    
print(answers)

for answer in answers:
    print(answer, end=' ')