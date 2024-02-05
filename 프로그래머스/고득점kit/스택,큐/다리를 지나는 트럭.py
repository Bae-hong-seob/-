from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge, truck_weights = deque(), deque(truck_weights)
    
    answer, sum_weight = 0,0
    while truck_weights:
        truck = truck_weights[0]
            
        if len(bridge) == bridge_length: #다리를 지난 경우
            sum_weight-=bridge.popleft()
            
        if sum_weight + truck <= weight: #트럭을 올릴 수 있을 때
            bridge.append(truck)
            sum_weight+=truck
            truck_weights.popleft()
        else:
            bridge.append(0)
        answer+=1
        
    answer+=bridge_length #마지막 트럭 통과
    
    return answer