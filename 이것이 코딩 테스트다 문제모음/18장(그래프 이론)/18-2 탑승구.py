G = 4 # 1 <= G <= 100,000 | 탑승구 수
P = 3 # 1 <= P <= 100,000 | 비행기 수
dokings = [4,1,1]

# G = 4 # 1 <= G <= 100,000 | 탑승구 수
# P = 6 # 1 <= P <= 100,000 | 비행기 수
# dokings = [2,2,3,3,4,4]

visited = [True for _ in range(G+1)] # 초기값은 다 도킹이 가능한 상태
visited[0] = False # 탑승구 위치는 1부터 G까지.

def check_doking(doking_index):
    if doking_index <= 0:
        return False
    
    if visited[doking_index]: # 도킹 가능할때는 True 반환
        visited[doking_index] = False # 방문처리
        return True
    else: # 도킹 불가능할 때는 index-1 탑승구 확인
        return check_doking(doking_index-1)
    

count = 0
for doking in dokings:
    if check_doking(doking): # 방문가능하다면
        print(doking, visited)
        count+=1
        
    elif count == G: # 모든 탑승구에 꽉 찬 경우 운행 중지.
        break
    
    else: # 1~g(i)까지는 다 찬 경우
        break
    
print('final : ', visited)
print(count)