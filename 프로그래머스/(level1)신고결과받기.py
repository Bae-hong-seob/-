id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
# 정답 answer = [2,1,1,0]

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3
# # 정답 answer = [0,0]

# id_list 와 신고한 이용자의 ID 정보가 담긴 배열 report, 정지 기준이 되는 신고 횟수 k 가 주어진다
# 따라서 def solution 안에 작성하면 됨.

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    index_list = [0]*len(id_list)
    
    # 한 유저가 같은 유저를 여러번 신고한 경우는 신고 횟수 1회로 처리
    report = set(report)
    
    for i in report:
        index_list[id_list.index(i.split()[1])] += 1
        
    # i 는 index_list 에서 k 이상 신고된 사람 index를 관리하기 위한 변수 
    i = 0
    over_k_report_people_list = []
    for j in index_list:
        if j >= k:
            # id_list[i]는 k번 이상 신고된 사람
            over_k_report_people_list.append(id_list[i])
                
        i+=1
    
    if len(over_k_report_people_list) != 0:

        for l in report:
            if l.split()[1] in over_k_report_people_list:
                answer[id_list.index(l.split()[0])] +=1
    
    return answer

# ---------------------------------------------for문 두번은 되도록 쓰지말자. 시간초과 걸린다 ----------------------------------------


# best solution



# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer