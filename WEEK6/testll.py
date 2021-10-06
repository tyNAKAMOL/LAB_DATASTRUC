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
            return ""
        s = ''
        current = self.dummy_head.next
        while current.next != None:
            s += str(current.data) + "->" if current.next != self.dummy_tail else str(current.data)
            current = current.next
        return s

    def isEmpty(self) :
        return self.size == 0

    def append(self,item):
        newNode = Node(item)
        newNode.prev = self.dummy_tail.prev
        newNode.next = self.dummy_tail
        self.dummy_tail.prev.next = newNode
        self.dummy_tail.prev = newNode
        self.size+=1

    def addBefore(self,item):
        newNode = Node(item)
        newNode.prev = self.dummy_head 
        newNode.next = self.dummy_head.next
        self.dummy_head.next.prev = newNode
        self.dummy_head.next = newNode
        self.size+=1
        
    def str_reverse(self):
        if self.isEmpty():
            return ""
        s = ''
        current = self.dummy_tail.prev
        while current.prev != None:
            s += str(current.data) + "->" if current.prev != self.dummy_head else str(current.data)
            current = current.prev
        return s

    def remove(self,item):
        if self.isEmpty():
            return print("Not Found!")
        else:
            current = self.dummy_head.next
            index = -1
            while current is not None:
                index+=1
                if current.data == item:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    current.prev = None
                    current.next = None
                    self.size-=1
                    return print("removed :",item,"from index :",index)
                current = current.next
            return print("Not Found!")
            
    def insert(self,i,item):
        if i>=0 and i<=self.size:
            newNode = Node(item)
            current = self.dummy_head.next
            index = -1
            while current != None:
                index+=1
                if index == i:
                    break
                current = current.next
            current.prev.next = newNode
            newNode.prev = current.prev
            newNode.next = current
            current.prev = newNode
            self.size+=1
            return print("index =",index,"and data =",item)
        else:
            return print("Data cannot be added")

inp = input("Enter Input : ").split(',')
doubly = DoublyLinkedList()
for i in range(len(inp)): 
    split1 = inp[i].split() 
    num = split1[1] 

    if split1[0]=='A': 
        doubly.append(num)
    elif split1[0]=='Ab': 
        doubly.addBefore(num)
    elif split1[0] =='R':
        doubly.remove(num)
    elif split1[0] == 'I':
        num1,num2 = num.split(':')
        num1_int = int(num1)
        doubly.insert(num1_int,num2)
    
    print("linked list :",doubly)
    print("reverse :",doubly.str_reverse())