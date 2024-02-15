from collections import deque

def bfs(graph, start, distances):
    queue = deque()
    queue.append(start)
    
    while queue:
        now = queue.popleft()
        
        for neighbor in graph[now]:
            if distances[neighbor] <= distances[now]+1: #최소값이 아닌경우
                continue
            else:
                distances[neighbor] = distances[now]+1 #최소값 업데이트
                queue.append(neighbor)

def solution(begin, target, words):
    if target not in words: #반환할 수 없는 경우 예외처리
        return 0
    
    dictionary = {} #그래프 생성을 위해 단어:index mapping
    if begin not in words: #시작점이 주어진 단어안에 있을수도 없을수도 있음.
        dictionary[begin] = 0
        for idx, word in enumerate(words):
            dictionary[word] = idx+1
    else:
        for idx, word in enumerate(words):
            dictionary[word] = idx
    
    graph = [[] for _ in range(len(words)+1)]
    for word1 in dictionary: #최대 단어 50개. 각 단어길이는 최대 10. 50*50*10 = 25000.
        for word2 in dictionary:
            count = 0
            for i in range(len(word1)): #모든 단어 길이는 같음
                if word1[i] != word2[i]: #알파벳 다른 개수
                    count+=1
            if count ==1: #한 번에 한 개의 알파벳만 바꿀 수 있음 = 연결됨
                #양방향이지만 모든 단어를 탐색하므로 한번만 추가해도 됨
                graph[dictionary[word1]].append(dictionary[word2])
        
    distances = [len(dictionary)]*len(dictionary) #최소 거리 탐색을 위해 최대값으로 초기화
    distances[dictionary[begin]] = 0 #시작점은 거리 0

    bfs(graph, dictionary[begin], distances)
    if distances[dictionary[target]] == len(dictionary): #변환할 수 없는 경우
        return 0
    else:
        return distances[dictionary[target]]