class Node : 
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):                
        self.dummy_head = Node(None)
        self.dummy_tail = Node(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "3"
        s = ''
        current = self.dummy_head.next
        while current.next != None:
            s += str(current.data) + "->" if current.next != self.dummy_tail else str(current.data)
            current = current.next
        return s
    
    def isEmpty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size
    
    def push(self,item):
        newNode = Node(item)
        newNode.prev,newNode.next = self.dummy_tail.prev,self.dummy_tail
        self.dummy_tail.prev.next,self.dummy_tail.prev = newNode,newNode
        self.size += 1

    def popfront(self):
        value = self.dummy_head.next.data
        self.dummy_head.next.prev = None 
        self.dummy_head.next.next.prev = self.dummy_head
        self.dummy_head.next = self.dummy_head.next.next
        # self.dummy_head.next.next = None
        self.size-=1
        return value

L = DoublyLinkedList()
for i in range(5):
    L.push(i)
L.popfront()
print(L.getSize())
# print("POP ->",L.popfront())
# print("POP ->",L.popfront())
print(L)