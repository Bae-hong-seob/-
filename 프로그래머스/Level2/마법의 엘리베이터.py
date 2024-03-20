def remove_fives(fives):
    if len(fives)==0:
        return 0
    elif len(fives)==1:
        return 5
    else:
        return 5+4*(len(fives)-1)

def solution(storey):
    answer,a = 0,0
    fives = []
    for number in str(storey)[::-1]:
        number = int(number)+a
        if number == 5:
            fives.append(number)
            a=0 #올림 여부 모름
            continue
            
        if number>5:
            if fives: #뒤에 5가 쌓인경우
                number+=1 #무조건 올림하는게 좋음.
                answer+=remove_fives(fives)
                fives=[]
            answer+=(10-number)
            a=1
            
        elif number<5:
            up = remove_fives(fives) + number+1
            down = 5*len(fives)+number
            answer+=min(up,down)
            fives = []
            a=0
    if fives:
        if len(fives)>1:
            a=1
        else:
            a=0
        answer+=remove_fives(fives)
        
    if a>0:
        answer+=1
        
    return answer