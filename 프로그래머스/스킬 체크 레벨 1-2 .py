def solution(food):
    #len(food) : 음식의 종류 개수
    #food[i] : i번 음식의 수
    #food[0] : 물의 양. 항상 1


    num_list = []
    answer = ''

    for i in range(1,len(food)):
        num = food[i]
        num_list.append(int(num/2))
        answer += str(i)*(int(num/2))

    answer_reverse = "".join(reversed(answer))
    answer+='0'
    answer += answer_reverse


    return answer