class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0 

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
        else:
            current = self.head
            while current.next is not None: 
                current = current.next
            current.next = newNode
        self.size+=1

    def addHead(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
        else:
            current = self.head
            self.head,newNode.next = newNode,current
        self.size+=1

    def search(self, item):
        if self.isEmpty():
            return "Not Found"
        else:
            current = self.head
            while current is not None:
                if current.value == item:
                    return "Found"
                current = current.next
            if current is None:
                return "Not Found"

    def index(self, item):
        if self.isEmpty():
            return "-1"
        else:
            index_ = -1
            if self.search(item) == "Found":
                current = self.head
                while current is not None:
                    index_ += 1
                    if current.value == item:
                        break
                    current = current.next
            return index_

    def Size(self):
        return self.size

    def pop(self, pos):
        if self.isEmpty():
            return "Out of Range"
        elif pos == 0:
            current = self.head
            self.head,current.next = current.next,None
            self.size-=1
            return "Success"
        else:
            index_ = -1
            current = self.head
            prev = None
            while current is not None:
                index_+=1
                if index_ == pos:
                    prev.next,current.next = current.next,None 
                    return "Success"
                prev = current
                current = current.next
            self.size-=1
            return "Out of Range"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.Size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)