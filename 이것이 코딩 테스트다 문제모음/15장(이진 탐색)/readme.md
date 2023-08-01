~~~
from bisect import bisect_left, bisect_right

nums = [4, 5, 5, 5, 5, 5, 5, 5, 5, 6]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))


'''
결과값
1
9
'''
~~~

이진 탐색 -> bisect 라이브러리 사용하면 편리하게 구현할 수 있음.
