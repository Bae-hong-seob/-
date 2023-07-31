# N, C = 5,3 # 2 <= N <= 200000 , 2 <= C <= N
# houses = [1, 2, 8, 4, 9]

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

# solution
import heapq

houses.sort()

mininum = houses[-1] - houses[0]

# 가장 왼쪽과 오른쪽에는 무조건적으로 와이파이 설치.
def binary_search(array, start, end):    
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    distance = min(array[mid]-array[0], array[-1]-array[mid])
    return distance

C-=2 # 양쪽 끝에 공유기 설치
start, end = 0, N-1

distance = -1 * (houses[-1] - houses[0])
hq = [[distance, start, end]]
heapq.heapify(hq)

while C != 0: # 공유기 다 설치할 때 까지 반복
    distance, start, end = heapq.heappop(hq) # 공유기 사이를 최대로 하는 start, end point 출력.
    C-=1 # 공유기 설치
    
    if start >= end:
        continue
    
    mid = (start+end) // 2
    
    distance = min(houses[mid]-houses[start], houses[end]-houses[mid])
    mininum = min(mininum, distance)

    # 후보군 두개 생성
    mid_left = (start + mid) // 2
    mid_right = (mid + end) // 2
    #print('index : ', start, end, mid)
    #print('candidate index : ',mid_left, mid_right)
        
    distance_left = min(houses[mid_left] - houses[start], houses[mid]-houses[mid_left])
    #print('distance left : ', houses[mid_left],houses[start], houses[mid],houses[mid_left])
    distance_right = min(houses[mid_right]-houses[mid], houses[end]-houses[mid_right])    
    
    heapq.heappush(hq,[-1*distance_left, start, mid])
    heapq.heappush(hq,[-1*distance_right, mid, end])
    #print(hq)
    
print(mininum)