from collections import defaultdict

def solution(fees, records):
    parkings = defaultdict(list)
    
    answer = defaultdict(list)
    for record in records:
        time, number, process = record.split()
        if process == 'IN':
            parkings[number] = time
        
        else:
            in_hour, in_minute = parkings[number].split(':')
            out_hour, out_minute = time.split(':')
                
            total_minute = (int(out_hour)*60 + int(out_minute)) - (int(in_hour)*60 + int(in_minute))
            answer[number].append(total_minute)
            del parkings[number]
    
    for key, time in parkings.items(): #출차시간이 적히지 않은 경우 23:59로 계산
        in_hour, in_minute = time.split(':')
        out_hour, out_minute = 23, 59
        total_minute = (int(out_hour)*60 + int(out_minute)) - (int(in_hour)*60 + int(in_minute))
        answer[key].append(total_minute)
    
    result = []
    for key,value in answer.items():
        total_minute = sum(value)
        
        if total_minute <= fees[0]: #기본 시간 이하
            result.append([key, fees[1]])
            
        else:
            total_minute-=fees[0] #추가 시간 계산
            if total_minute%fees[2]==0: 
                result.append([key, fees[1] + fees[3]*(total_minute//fees[2])])
            else: #추가 시간은 올림 처리
                result.append([key, fees[1] + fees[3]*(total_minute//fees[2] + 1)])
    result.sort()
    return [fee for number,fee in result]