N, M = 4,6 # 1 <= N <= 1000000 , 1 <= M <= 20억
heights = [19, 15, 10, 17] # 각 높이는 0 이상 10억 이하

# # solution
# heights.sort()
# print(heights)

# i = 1
# while True:
#     now_height = heights[-1 * i] # 뒤에서부터 탐색
#     print(i, heights[-i:], sum([height - now_height for height in heights[-1*i:]]))
#     if sum([height - now_height for height in heights[-1*i:]]) >= M: # 자른 합이 M보다 클 경우
#         break
#     else:
#         i+=1

# if sum([height - now_height for height in heights[-1*i:]]) == M: # 자른 합이 딱 맞을 경우
#     print(now_height)
    
# else: # 아닐 경우 최대 높이 조정
#     while(sum([height - now_height for height in heights[-1*i:]]) != M):
#         now_height+=1
#     print(now_height)
    
# 이진탐색 solution
start = 0
end = max(heights)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2
    
    for x in heights:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
            
    # 떡의 양이 부족한 경우 더 많이 자르기(=왼쪽 부분 탐색)
    if total < M:
        end = mid -1
        
    # 떡의 양이 충분한 경우 덜 자르기(=오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기에서 result에 기록
        start = mid + 1
        
print(result)