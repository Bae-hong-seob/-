# 삼성 코딩테스트는 itertools 라이브러리 사용이 안되는 관계로 조합,순열은 직접 만들 줄 알아야한다.

## 조합(combinations) 구현
~~~
arr = [1,2,3,4,5]
candidates = []

def combinations(n,new_arr,c):
    global arr
    if len(new_arr)==n:
        candidates.append(new_arr)
        return new_arr
    for i in range(c,len(arr)):
        combinations(n,new_arr+[arr[i]],i+1)

combinations(n,[],0)
~~~

## 순열(permutations) 구현
~~~
arr = [1,2,3,4,5]
visited = [False]*len(arr)
candidates = []

def permutations(n,new_arr):
    global arr, candidates
    if len(new_arr)==n:
        candidates.append(new_arr)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i]=True
            permutations(n,new_arr+[arr[i]])
            visited[i]=False

permutations(n,[])
~~~

## 중복순열(product) 구현
~~~
arr = [1,2,3,4,5]
candidates=[]

def product(n,new_arr):
    global arr,candidates
    if len(new_arr)==n:
        candidates.append(new_arr)
        return

    for i in range(len(arr)):
        product(n,new_arr+[arr[i]])


product(n,[])
~~~

## 중복 조합(combinations_with_replacement)
~~~
arr = [i for i in range(1,N+1)]
candidates = []

def combinations_with_replacement(n,new_arr,c):
    if len(new_arr)==n:
        candidates.append(new_arr)
        return

    for i in range(c,len(arr)):
        combinations_with_replacement(n,new_arr+[arr[i]],i)

combinations_with_replacement(n,[],0)
~~~


## 배열 회전
- 90도 회전 : 가로,세로 길이가 바뀜
~~~
def rotation(original):
    N,M = len(original), len(original[0])
    result = [[0]*n for _ in range(M)]

    for i in range(N):
        for j in range(M):
            result[j][n-i-1] = origianl[i][j]

    return result
~~~

- 180도 회전 : 가로,세로 길이가 일정
~~~
def rotation(original)
    N,M = len(original), len(original[0])
    result = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            result[n-i-1][m-j-1] = original[i][j]

    return result
~~~
