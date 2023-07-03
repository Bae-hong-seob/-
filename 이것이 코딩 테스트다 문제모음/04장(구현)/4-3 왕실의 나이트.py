N = 'a1'

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] #x
rows = ['1','2','3','4','5','6','7','8'] #y

moves = [[1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1], [-2,1], [-1,2]] #8가지 move 경우의 수

for x,y in N.split():
            print(x,y)
            x = columns.index(x)
            y = rows.index(y)
            print(x,y)
            
answer = 0
            
for move in moves:
            nx, ny = move
            new_x = x - nx
            new_y = y - ny
            
            if new_x < 0 or new_x > 7 or new_y < 0 or new_y > 7: # 체스판을 벗어난 경우
                        continue
            else:
                        answer+=1
                        
print(answer)