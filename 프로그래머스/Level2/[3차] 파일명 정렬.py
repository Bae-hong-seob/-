def solution(files):
    idx2file = {}
    for idx, file in enumerate(files):
        idx2file[idx] = file
    
    numbers = [str(i) for i in range(10)]
    answer = []
    for idx, file in enumerate(files):
        head, number, tail = '','',''
        number_count = 0
        for char in file:
            if char not in numbers:
                if len(number)==0: #number가 비었다면 아직 head에 위치
                    head+=char
                else:
                    tail+=char
            else: #숫자가 나타났는데 number일수도 tail일수도.
                if len(number)<5 and len(tail)==0: #number는 연속된 숫자 & tail 시작전
                    number+=char
                else:
                    tail+=char

        
        head, tail = head.lower(), tail.lower()
        dict_number = '0'*(5-len(number)) + number
        answer.append([head, dict_number, idx]) #[첫번째 정렬 기준(사전 이름), 두번째 정렬 기준(기존 순서)]
    return [idx2file[idx] for file_name, dict_number, idx in sorted(answer)]