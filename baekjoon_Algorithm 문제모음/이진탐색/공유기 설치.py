N,C = 5,3
houses = [1,2,8,4,9]

N,C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort() #최대 10**9 이므로 시간복잡도 log(10**9)하면 9.

'''
    keypoint: 공유기 거리를 이진탐색으로 찾기.
'''

start,end = 1, houses[-1]-houses[0]
answer = 0

while start<=end:
    pivot=(start+end)//2
    before_wifi = houses[0]
    
    count=1 #공유기 개수 세기. 가운데에 설치했다고 가정.
    for i in range(N):
        if houses[i]-before_wifi>=pivot: # 공유기가 닿을 수 없다면 새로 설치
            count+=1
            before_wifi=houses[i]
            
    if count>C: #공유기가 더 많이 필요한 경우 최소 거리를 늘려야함.
        start=pivot+1
    elif count==C: #알맞게 설치한 경우 거리를 조금 더 늘려본다.
        start=pivot+1
        answer=pivot
    else: #공유기가 부족한 경우 최소 거리를 줄여야함.
        end=pivot-1
    
    

print(answer)