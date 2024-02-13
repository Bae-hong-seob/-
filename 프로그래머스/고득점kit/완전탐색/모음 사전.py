from itertools import permutations, product, combinations, combinations_with_replacement

def solution(word):
    #print(6**5) #완전탐색 시간복잡도 확인 ['', 'A', 'E', 'I', 'O', 'U'] 중 5자리
    words = ['A', 'E', 'I', 'O', 'U']
    dictionary = set()
    for i in range(1, 6): #word길이는 1이상 5이하
        for candidate in combinations_with_replacement(words, i):
            for new_word in permutations(candidate):
                new_word = ''.join(new_word)
                dictionary.add(new_word)
            
    dictionary = list(dictionary)
    dictionary.sort()
    #print(len(dictionary)) #전체 사전크기 확인
    for idx, candidate in enumerate(dictionary):
        if candidate == word:
            return idx+1
