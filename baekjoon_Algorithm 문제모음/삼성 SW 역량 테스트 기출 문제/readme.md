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
~~~
