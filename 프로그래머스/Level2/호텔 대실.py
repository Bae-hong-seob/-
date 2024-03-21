from collections import deque

def solution(book_time):
    book_time.sort()
    booking = []
    for start, end in book_time: #최대 1,000번.
        start_hour, start_minute = int(start[:2]), int(start[-2:])
        end_hour, end_minute = int(end[:2]), int(end[-2:])
        
        end_minute+=10 #퇴장시간 10분은 청소시간.
        if end_minute>=60:
            end_hour+=1
            end_minute = end_minute-60
        if not booking: #아무방도 사용중이지 않은 경우
            booking.append(deque([[end_hour, end_minute]]))
        else:
            add = True
            for dq in booking: # 최대 1000번 -> 1,000,000 완전탐색 가능.
                available_hour, available_minute = dq[-1]
                if available_hour < start_hour: #해당 방에 입장 가능한 경우
                    dq.popleft()
                    dq.append([end_hour, end_minute])
                    add=False
                    break
                elif available_hour<=start_hour and available_minute <= start_minute: #해당 방에 입장 가능한 경우
                    dq.popleft()
                    dq.append([end_hour, end_minute])
                    add=False
                    break
                else:
                    continue
                    
            if add:
                booking.append(deque([[end_hour, end_minute]]))
                    
            
    return len(booking)