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

    def pop(self):
        if self.isEmpty():
            self.head = None
        else:
            prev = None
            current = self.head
            while current is not None:
                if current.next is None:
                    if prev is None:
                        self.head = None
                        return current.value
                    else:
                        prev.next = None
                        return current.value
                prev = current
                current = current.next
        self.size-=1

    def addHead(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
        else:
            current = self.head
            self.head,newNode.next = newNode,current
        self.size+=1
    
    def Size(self):
        return self.size

L1 = LinkedList()
L2 = LinkedList()
inp = input("Enter Input (L1,L2) : ").split()
l1 = inp[0].split("->")
l2 = inp[1].split("->")
for i in l1:
    if i not in "->":
        L1.append(i)
for i in l2:
    if i not in "->":
        L2.append(i)
print("L1    :",L1)
print("L2    :",L2)
x=L2.Size()
for i in range(x):
    L1.append(L2.pop())
print("Merge :",L1)
