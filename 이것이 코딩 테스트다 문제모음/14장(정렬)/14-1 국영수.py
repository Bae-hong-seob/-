# N = 12
# students = [ # 이름, 국어, 영어, 수학 점수 순서
#     ['Junkyu', 50, 60, 100],
#     ['Sangkeun', 80, 60, 50],
#     ['Sunyoung', 80, 70, 100],
#     ['Soong', 50, 60, 90],
#     ['Haebin', 50, 60, 100],
#     ['Kangsoo', 60, 80, 100],
#     ['Donghyuk', 80, 60, 100],
#     ['Sei', 70, 70, 70],
#     ['Wonseob', 70, 70, 80],
#     ['Sanghyun', 70, 70, 80],
#     ['nsj', 80, 80, 80],
#     ['Taewhan', 50, 60, 90]
#     ]

N = int(input())
students = []
for _ in range(N):
    students.append(list(input().split()))

for student in students: # 하나는 오름차순, 하나는 내림차순이라면 그냥 -1 곱해버리고 오름차순 통일해버리면 됨.
    student[1] = int(student[1]) * (-1)
    student[3] = int(student[3]) * (-1)
    
students = sorted(students, key = lambda x : (x[1], x[2], x[3], [0]))


for student in students:
    print(student[0])