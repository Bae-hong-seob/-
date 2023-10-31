import copy

def check_available(graph):
    # print()
    # print('checking')
    # for row in reversed(graph):
    #     print(row)
    # print()
    for row, row_value in enumerate(graph):
        for column, column_value in enumerate(row_value):
            if len(column_value)==0:
                continue
                
            for value in column_value:
                if value == '기둥':
                    if row == 0:
                        continue
                        
                    if '기둥' in graph[row-1][column] or '보' in graph[row][column]:
                        continue
                    else:
                        return False
                elif value == '보':
                    if '기둥' in graph[row-1][column] or ('보' in graph[row][column-1] and '보' in graph[row][column+1]):
                        continue
                    else:
                        return False
                    
    return True
                        

def build(graph, column,row, command):
    if command == 0: # 기둥
        if row == 0: # 바닥에 설치하는 경우
            graph[row][column].append('기둥')
        else: # 2층 이상인 경우 밑에 기둥이나 보가 설치되어 있어야 가능
            if '기둥' in graph[row-1][column] or '보' in graph[row][column]:
                graph[row][column].append('기둥')
                
    elif command == 1: # 보
        if '기둥' in graph[row-1][column] or '기둥' in graph[row-1][column+1] or ('보' in graph[row][column-1] and '보' in graph[row][column+1]):
            graph[row][column].append('보')
            graph[row][column+1].append('보')
                
    return graph

def delete(graph, column,row, command):
    tmp_graph = copy.deepcopy(graph)
    
    result = True
    if command == 0: # 기둥
        tmp_graph[row][column].remove('기둥')
        result = check_available(tmp_graph)
    elif command == 1: #보
        for row_idx, row_value in enumerate(tmp_graph):
            for column_idx, column_value in enumerate(row_value):
                if len(column_value) == 0:
                    continue

                for value in column_value:
                    if value == '보':
                        tmp_graph[row_idx][column_idx+1].remove('보')
        
        # print('sort')
        # print(row, column, tmp_graph[row][column], '보' in tmp_graph[row][column])
        try:
            tmp_graph[row][column].remove('보')
        except:
            tmp_graph[row][column] = []
            
        # for row in reversed(tmp_graph):
        #     print(row)
        # print()
        
        result = check_available(tmp_graph)
    
    # print('delete : ', result)
    # print(graph == tmp_graph)
    if result == False:
        return graph
    else:
        return tmp_graph

def solution(n, build_frame):
    graph = [[[] for _ in range(n+1)] for _ in range(n+1)]
    for column,row, a,b in build_frame:
        if b == 0:
            graph = delete(graph, column,row, a)
        elif b == 1:
            graph = build(graph, column,row, a)
        else:
            print('input error')
    
    # print('final graph')
    # for row in reversed(graph):
    #     print(row)
        
    answer = []
    for row_idx, row_value in enumerate(graph):
        for column_idx, column_value in enumerate(row_value):
            if len(column_value) == 0:
                continue
            
            for value in column_value:
                if value == '보':
                    graph[row_idx][column_idx+1].remove('보')
    # print()
    # for row in reversed(graph):
    #     print(row)
        
    for row_idx, row_value in enumerate(graph):
        for column_idx, column_value in enumerate(row_value):
            if len(column_value) == 0:
                continue
            
            for value in column_value:
                if value == '기둥':
                    answer.append([column_idx, row_idx, 0])
                elif value == '보':
                    answer.append([column_idx, row_idx, 1])
    answer.sort()
    return answer