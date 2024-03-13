def install(start_number, min_range, w):
    if (min_range-start_number)%(2*w+1)==0:
        return (min_range-start_number)//(2*w+1)
    else:
        return (min_range-start_number)//(2*w+1)+1
        

def solution(n, stations, w):
    answer = 0
    
    start_number = 1 #아파트 1번부터 탐색 시작
    for station in stations: #최대 10,000번
        min_range, max_range = station-w, station+w
        if min_range < 1: #최소 아파트 번호는 1
            min_range = 1
        if max_range > n: #최대 아파트 번호는 n
            max_range = n
        #print(f'wifi in {min_range} to {max_range}')
        answer+=install(start_number, min_range, w)
        start_number = max_range+1
    
    if max_range < n:
        if start_number==n: #마지막에 기지국 하나만 설치하면 됨.
            answer+=1
        else:
            answer+=install(start_number, n, w)
    
    return answer