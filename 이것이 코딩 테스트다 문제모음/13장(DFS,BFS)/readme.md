~~~
from itertools import combinations # 조합(부분집합)
from itertools import permutations # 순열
~~~

기억하기 itertools.  

#### DFS,BFS는 재귀문(stack), while(queue) 이므로... 매 타임마다 graph 크기만큼 past를 생성하는 행위는 좋지 않음.  
- visited 변수를 매번 생성할 시 시간초과 뜰 확률이 높아짐. (13-7 인구 이동 문제)
