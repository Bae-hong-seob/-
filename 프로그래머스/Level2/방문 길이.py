from collections import defaultdict

def solution(dirs):
    visited= defaultdict(list)
    drow, dcolumn = [0,-1,0,1],[1,0,-1,0] #우,상,좌,하
    row,column = 0,0
    
    answer = 0
    for direction in dirs:
        if direction == 'R': #우
            move_row, move_column = row+drow[0], column+dcolumn[0]
            if move_row < -5 or move_row > 5 or move_column < -5 or move_column > 5: #지도를 벗어나는 경우
                continue
            
            if 'L' in visited[move_row,move_column]: #이미 거쳐간 길인 경우
                row,column = move_row,move_column
            else:
                visited[row,column].append('R')
                visited[move_row,move_column].append('L')
                answer+=1
                
        elif direction == 'U': #상
            move_row, move_column = row+drow[1], column+dcolumn[1]
            if move_row < -5 or move_row > 5 or move_column < -5 or move_column > 5: #지도를 벗어나는 경우
                continue
            if 'D' in visited[move_row,move_column]: #이미 거쳐간 길인 경우
                row,column = move_row,move_column
            else:
                visited[row,column].append('U')
                visited[move_row,move_column].append('D')
                answer+=1
                
        elif direction == 'L': #좌
            move_row, move_column = row+drow[2], column+dcolumn[2]
            if move_row < -5 or move_row > 5 or move_column < -5 or move_column > 5: #지도를 벗어나는 경우
                continue
            if 'R' in visited[move_row,move_column]: #이미 거쳐간 길인 경우
                row,column = move_row,move_column
            else:
                visited[row,column].append('L')
                visited[move_row,move_column].append('R')
                answer+=1
                
        elif direction == 'D': #하
            move_row, move_column = row+drow[3], column+dcolumn[3]
            if move_row < -5 or move_row > 5 or move_column < -5 or move_column > 5: #지도를 벗어나는 경우
                continue
            if 'U' in visited[move_row,move_column]: #이미 거쳐간 길인 경우
                row,column = move_row,move_column
            else:
                visited[row,column].append('D')
                visited[move_row,move_column].append('U')
                answer+=1
                    
        else:
            raise Exception('입력이 잘못되었습니다.')
        
        row,column = move_row,move_column
                
                
    return answer