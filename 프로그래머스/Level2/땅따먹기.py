def solution(land):
    dp_table = [[0]*4 for _ in range(len(land))]
    
    for row_idx, row in enumerate(land): #최대 100,000            
        for idx1, value in enumerate(row): #최대 4 -> 400,000 완전탐색 가능
            for idx2, ex_value in enumerate(dp_table[row_idx-1]): #최대 4 -> 1,600,000 완전탐색 가능.
                if idx1==idx2:
                    continue
                else:
                    dp_table[row_idx][idx1] = max(dp_table[row_idx][idx1], ex_value+value)
                    
        # for x in dp_table:
        #     print(x)
        # print()          
    
    return max(dp_table[-1])