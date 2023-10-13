def solution(routes):
    routes.sort(key=lambda x:x[1])
    camera = []
    
    for route in routes:
        start, end = route
        if len(camera) == 0:
            camera.append(end)
            continue
        
        if camera[-1] < start:
            camera.append(end)
    return len(camera)