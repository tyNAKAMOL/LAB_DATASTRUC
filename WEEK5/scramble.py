class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    Dummy = Node(None)
    Dummy.next = Node(LL[0])
    current = Dummy.next
    for i in LL[1:]:
        current.next = Node(i)
        current = current.next
    current.next = None
    return Dummy.next

def printLL(head):
    current, string = head, str(head.value) + " "
    while current.next is not None:
        string += str(current.next.value) + " "
        current = current.next
    return string

def SIZE(head):
    current = head
    count = 0
    while current:
        count+=1
        current = current.next
    return count

def Riffle(h1, h2):
    Dummy = Node(None)
    current = Dummy
    while True:
        if h1 is None:
            current.next = h2
            break
        if h2 is None:
            current.next = h1
            break
        current.next = h1
        h1 = h1.next
        current = current.next
        current.next = h2
        h2 = h2.next
        current = current.next
    return Dummy.next

def Deriffle(LL,n):
    Len = SIZE(LL)
    Dummy1 = Node(None)
    Dummy2 = Node(None)
    cur1 = Dummy1              
    cur2 = Dummy2              
    current = LL 
    while True:
        if SIZE(Dummy1.next) == n:
            cur2.next = current
            break
        if SIZE(Dummy2.next) == Len-n:
            cur1.next = current
            break
        cur1.next = current 
        current = current.next 
        cur1,cur1.next = cur1.next,None 
        cur2.next = current 
        current = current.next 
        cur2,cur2.next = cur2.next,None 
    return Dummy1.next,Dummy2.next

def BottomUp(head, n):
    current = head
    for i in range(1,n):
        current = current.next
    head2,current.next = current.next,None
    return head,head2

def link(head1,head2):
    current = head1
    while current.next:
        current = current.next
    current.next = head2
    return head1

def scarmble(head, b, r, size):
    l = size
    inb_ = int(l*(b/100))
    inr_ = int(l*(r/100))
    h1,h2 = BottomUp(head,inb_)
    print("BottomUp {:.3f} % : {}{}".format(b,printLL(h2),printLL(h1)))
    h1,h2 = BottomUp(link(h2,h1),inr_)
    newList = Riffle(h1,h2)
    print("Riffle {:.3f} % : {}".format(r,printLL(newList)))
    h1,h2 = Deriffle(newList,inr_)
    print("Deriffle {:.3f} % : {}{}".format(r,printLL(h1),printLL(h2)))
    h1,h2 = BottomUp(link(h1,h2),l-inb_)
    LinkedListStart = link(h2,h1)
    print("Debottomup {:.3f} % : {}".format(b,printLL(LinkedListStart)))

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)


