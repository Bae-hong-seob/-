# N = 3 # 1 <= N <= 100000
# number_of_cards = [10,20,40]

N = int(input())
number_of_cards = []
for _ in range(N):
    number_of_cards.append(int(input()))

import heapq

heapq.heapify(number_of_cards)

count = 0
while len(number_of_cards) != 1: #
    first = heapq.heappop(number_of_cards)
    second = heapq.heappop(number_of_cards)
    
    sum_of_card = first + second
    count+=sum_of_card
    
    heapq.heappush(number_of_cards, sum_of_card)
    
print(count)    