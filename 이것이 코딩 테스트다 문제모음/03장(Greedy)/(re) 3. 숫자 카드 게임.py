# N, M = 3,3
# map = [
#     [3,1,2],
#     [4,1,4],
#     [2,2,2]
# ]

N, M = 2,4
map = [
    [7,3,1,8],
    [3,3,3,4]
]

max = 0
for row in map:
    value = min(row)
    if value > max:
        max = value
        
print(max)