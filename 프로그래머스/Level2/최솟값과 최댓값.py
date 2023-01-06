def solution(s):
    num_list = s.split()
    num_list = list(map(int, num_list))
    min_num = min(num_list)
    max_num = max(num_list)
    
    answer = str(min_num) + " " + str(max_num)
    return answer