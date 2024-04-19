def solution(words, queries):
    head, head_rev = {},{}
    lengths = []
    
    def tries(head, word):
        node = head
        for w in word:
            if w not in node:
                node[w]={}
            node = node[w]
            if 'len' not in node:
                node['len'] = [len(word)]
            else:
                node['len'].append(len(word))
        node['end']=True
        
    for word in words:
        tries(head,word)
        tries(head_rev,word[::-1])
        lengths.append(len(word))
        
    def serach(query):
        if query[-1]=='?': # 접미사 ? 인 경우
            node = head
        elif query[0]=='?': # 접두사 ? 인 경우
            node = head_rev
            query=query[::-1]
        else:
            raise Exception('Something Wrong !!!')
            
        for q in query:
            if q=='?': # ?를 만난다면 종료, ?는 하나 이상 포함되어 있음.
                return node['len'].count(len(query))

            if q not in node: # 매치되는 가사가 없는 경우
                return 0
            node = node[q]

    
    answer = []
    for query in queries:
        if query[0]=='?' and query[-1]=='?':
            answer.append(lengths.count(len(query)))
            continue
        
        answer.append(serach(query))
    
    return answer