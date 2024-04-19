N=5
numbers = [-15, -6, 1,3,7] #서로 다른 원소. 모든 원소 오름차순

N=7
numbers = [-15,-4,2,8,9,13,15]

N=7
numbers=[-15,-4,3,8,9,13,15]
'''
    고정점은 반드시 하나다. 라는 문구가 없다?
    여러개라면 어떻게 출력할지 정해놓지도 않았다.
'''

pivot = N//2
left,right = 0,N-1

available=True
while pivot!=numbers[pivot]:
    if left>=right:
        available=False
        break
    
    if pivot>numbers[pivot]:
        left=pivot+1
        pivot = (left+right)//2
    else:
        right=pivot-1
        pivot = (left+right)//2

if available:   print(pivot)
else: print(-1)