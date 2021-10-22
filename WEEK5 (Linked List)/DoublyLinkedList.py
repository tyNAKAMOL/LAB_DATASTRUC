class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    def __str__(self):
        if self.isEmpty():
            return ""
        cur, s = self.head, ""
        while cur is not None:
            s += str(cur.value) + "->" if cur.next is not None else str(cur.value)
            cur = cur.next
        return s
    
    def str_reverse(self):
        if self.isEmpty():
            return ""
        cur, s = self.tail,""
        while cur is not None:
            s += str(cur.value) + "->" if cur.prev is not None else str(cur.value)
            cur = cur.prev
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            current = self.tail
            current.next,newNode.prev,self.tail = newNode,current,newNode
        self.size += 1
    
    def add_before(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            current = self.head
            current.prev,newNode.next,self.head = newNode,current,newNode
        self.size += 1
    
    def Size(self):
        return self.size         

    def insert(self,index,value):
        if 0<=index<=self.size:
            newNode = Node(value)
            if index == 0:
                if self.isEmpty():
                    self.head = newNode
                    self.tail = newNode
                else:
                    current = self.head
                    self.head,newNode.next,current.prev = newNode,current,newNode
                self.size+=1
                return "index = {0} and data = {1}".format(index, value)
            elif index == self.size: 
                current = self.tail
                current.next,newNode.prev,self.tail = newNode,current,newNode
                self.size+=1
                return "index = {0} and data = {1}".format(index, value)
            else:
                current = self.head
                prev = None
                index_ = -1
                while current:
                    index_+=1
                    if index_ == index:
                        prev.next,current.prev,newNode.prev,newNode.next = newNode,newNode,prev,current
                        self.size+=1
                        return "index = {0} and data = {1}".format(index, value)
                    prev = current
                    current = current.next
        else: return "Data cannot be added"

    def remove(self,item):
        if self.isEmpty():
            return "Not Found!"
        else:
            current = self.head
            if current.value == item:
                if self.size==1:
                    self.head = None
                    self.tail = None
                else:
                    newCur = current.next
                    self.head,current.next = current.next,None
                    newCur.prev = None
                self.size-=1
                return "removed : "+str(item)+" from index : 0"
            else:
                prev_ = None
                index_ = -1
                while current:
                    index_ += 1
                    if current.value == item:
                        if index_ == self.size-1:
                            self.tail,prev_.next,current.prev = current.prev,None,None
                        else:
                            newCur = current.next
                            prev_.next,current.next,current.prev,newCur.prev = current.next,None,None,prev_
                        self.size-=1
                        return  "removed : "+str(item)+" from index : " + str(index_)
                    prev_ = current
                    current = current.next
                return "Not Found!"

L=LinkedList()
inp = input("Enter Input : ").split(',')
inp = [i.strip() for i in inp]
for i in inp:
    if i[:2].strip() == "A":
        L.append(i[2:])
        print("linked list : {0}".format(L))
        print("reverse : {0}".format(L.str_reverse()))
    elif i[:3].strip() == "Ab":
        L.add_before(i[3:])
        print("linked list : {0}".format(L))
        print("reverse : {0}".format(L.str_reverse()))
    if i[:2].strip() == "I":
        print(L.insert(int(i[2:].split(":")[0]),i[2:].split(":")[1]))
        print("linked list : {0}".format(L))
        print("reverse : {0}".format(L.str_reverse()))
    elif i[:2].strip() == "R":
        print("{0}".format(L.remove(i[2:])))
        print("linked list : {0}".format(L))
        print("reverse : {0}".format(L.str_reverse()))
