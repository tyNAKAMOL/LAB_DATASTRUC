class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.Dummy_tail = Node(None)
        self.Dummy_head = Node(None)
        self.Dummy_head.next = self.Dummy_tail
        self.Dummy_tail.prev = self.Dummy_head
        self.size = 0 

    def __str__(self):
        if self.isEmpty():
            return ""
        s = ''
        current = self.Dummy_head.next
        while current.next != None:
            s += str(current.data) + "->" if current.next != self.Dummy_tail else str(current.data)
            current = current.next
        return s

    def isEmpty(self):
        return self.size == 0
    
    def len(self):
        return self.size

    def append(self, item):
        newNode = Node(item)
        newNode.prev,newNode.next = self.Dummy_tail.prev,self.Dummy_tail
        self.Dummy_tail.prev.next,self.Dummy_tail.prev = newNode,newNode
        self.size += 1
    
    def Insert(self,index,item):
        newNode = Node(item)
        current = self.Dummy_head
        index_ = -1
        while current:
            index_ += 1
            if index_ == index:
                break
            current = current.next
        newNode.prev,newNode.next = current,current.next
        current.next.prev,current.next = newNode,newNode
        self.size += 1
    
    def Left(self):
        try:
            current = self.Dummy_head.next
            while current:
                if current.value == '|' and current.prev is not self.Dummy_head:
                    break
                current = current.next
            current.value,current.prev.value = current.prev.value,current.value
        except:
            pass
    
    def Right(self):
        try:
            current = self.Dummy_head.next
            while current:
                if current.value == '|'and current.next is not self.Dummy_tail:
                    break
                current = current.next
            current.value,current.next.value = current.next.value,current.value
        except:
            pass
    
    def Backspace(self):
        try:
            current = self.Dummy_head.next
            while current:
                if current.value == '|':
                    break
                current = current.next
            current.prev.prev.next,current.prev.next = current,None
            current.prev.prev,current.prev = None,current.prev.prev
        except:
            pass
    
    def Delete(self):
        try:
            current = self.Dummy_head
            while current:
                if current.value == '|':
                    break
                current = current.next
            current.next.next.prev, current.next.prev = current, None
            current.next.next, current.next = None,current.next.next
        except:
            pass
    
    def index_cursor(self):
        current = self.Dummy_head.next
        index_ = -1
        while current:
            index_ += 1
            if current.value == '|':
                return index_
            current = current.next

L = LinkedList()
inp = input("Enter Input : ").split(',')
inp = [i.strip() for i in inp]
L.append("|")
for i in inp:
    if i[0] == "I":
        L.Insert(L.index_cursor(),i[2:])
    elif i[0] == "L":
        L.Left()
    elif i[0] == "R":
        L.Right()
    elif i[0] == "B":
        L.Backspace()
    elif i[0] == "D":
        L.Delete()
print(L)

