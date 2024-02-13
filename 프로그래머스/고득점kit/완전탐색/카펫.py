def solution(brown, yellow):
    
    candidates = []
    for width in range(1, yellow+1):
        if yellow%width == 0 and width >= yellow//width:
            candidates.append([width, yellow//width])
    
    for width,height in candidates: #yellow 카펫 후보군
        need_brown = (width+2)*2 + (height*2)
        if need_brown == brown:
            return [width+2,height+2] #최종 카펫 크기
