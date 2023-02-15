# Tree

Directed Graph의 일종.
![image](https://user-images.githubusercontent.com/49437396/218906291-1c8bc67c-7f75-4f15-80d8-160ae82d9f89.png)

## BFS : popleft(), append()의 연속
1. Queue A
2. Queue B,C,D
3. Queue C,D,F
4. Queue D,F
5. Queue F,E
6. Queue E,G
7. Queue G
8. Queue

## DFS : stack
1. Stack A
2. Stack A,B
3. Stack A,B,F
4. Stack A,B,F,C (갈수있는 곳이 없으면 pop 진행)
5. Stack A,B,F,G
6. Stack A,B,F
7. Stack A,B
8. Stack A
9. Stack A,D
10. Stack A,D,E
11. Stack A,D
12. Stack A
13. Stack 
