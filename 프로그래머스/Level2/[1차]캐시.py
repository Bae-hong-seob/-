#LRU 알고리즘 출처 : https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
#해당 코테 검색가능.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
class DoublyLinkedList:
    def __init__(self, cacheSize):
        self.cacheSize = cacheSize
        self.head = Node("")
        self.tail = Node("")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0
    
    def LRU(self, data):
        # print("[Put " + data + "]",self.count, end=" ")
        node = self.head.next
        while(node.data):
            if node.data == data:
                self.cacheHit(node, data)
                return self.count
            node = node.next
        self.cacheMiss(data)
        return self.count
    # 원소 맨앞으로 이동
    def cacheHit(self, node, data):
        self.removeNode(node)
        self.addFront(data)
        # print("[Hit ]", end=" ")
        self.count=1
        self.printAll()
    
    # node 삭제
    def removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    # head 의 바로 뒤에 원소 넣기
    def addFront(self, data):
        newNode = Node(data)
        self.head.next.prev = newNode
        newNode.next = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        
    # 원소의 맨앞에 추가 (cacheSize 보다 커지면 tail에 가까운 노드 삭제)
    def cacheMiss(self, data):
        self.addFront(data)
        if self.totalLen() > self.cacheSize:
            self.removeTail()
        # print("[Miss]", end=" ")
        self.count=5
        self.printAll()
        
    # linked list 의 총 길이 반환
    def totalLen(self):
        answer = 0
        node = self.head.next
        while(node.data):
            answer += 1
            node = node.next
        return answer
        
    # tail 에 가장 가까운 원소 삭제
    def removeTail(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        
    # head 부터 tail 까지 순환하면서 date 전부 출력
    def printAll(self):
        node = self.head.next
        while(node.data):
            # print(node.data, end="")
            node = node.next
            if (node.data):
                pass
        #         print(" -> ", end="")
        # print()

def solution(cacheSize, cities):
    test = DoublyLinkedList(cacheSize)
    inputArray = [city.lower() for city in cities]
    answer = 0
    for input in inputArray:
        answer+=test.LRU(input)
    return answer