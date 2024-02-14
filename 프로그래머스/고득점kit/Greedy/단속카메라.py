def solution(routes):
    routes.sort(key=lambda x:x[1])
    print(routes)
    cameras = []
    for start, end in routes:
        if len(cameras) == 0: 
            cameras.append(end) #최대한 다른 자동차도 감지할 수 있도록 출구에 배치
            continue
            
        if start <= cameras[-1] <= end: #이전에 설치한 카메라로도 감시 가능할 때
            continue
        else:
            cameras.append(end)
    
    return len(cameras)