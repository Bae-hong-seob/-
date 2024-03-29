N = 2
numbers = [5,6]
operations = [0,0,1,0]

N = 3
numbers = [3,4,5]
operations = [1,0,1,0]

N = 6
numbers = [1,2,3,4,5,6]
operations = [2,1,1,1]

N = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))

max_value, min_value = int(-1e9), int(1e9)
def dfs(stack, operations, result):
    global max_value,min_value
    if len(stack)==N:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    
    if operations[0]>0:
        dfs(stack+['+'], [operations[0]-1, operations[1], operations[2], operations[3]], result+numbers[len(stack)])
    if operations[1]>0:
        dfs(stack+['-'], [operations[0], operations[1]-1, operations[2], operations[3]], result-numbers[len(stack)])
    if operations[2]>0:
        dfs(stack+['*'], [operations[0], operations[1], operations[2]-1, operations[3]], result*numbers[len(stack)])
    if operations[3]>0:
        if result>0:
            dfs(stack+['/'], [operations[0], operations[1], operations[2], operations[3]-1], result//numbers[len(stack)])
        else:
            dfs(stack+['/'], [operations[0], operations[1], operations[2], operations[3]-1], -((-result)//numbers[len(stack)]))
            
dfs(['start'], operations, numbers[0])
print(max_value)
print(min_value)