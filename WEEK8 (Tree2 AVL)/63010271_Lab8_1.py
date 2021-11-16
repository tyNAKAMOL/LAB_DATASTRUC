class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            print("*")
        else:
            current = self.root
            while current:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        print("L*",end='')
                        break
                    else:
                        print("L",end='')
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data)
                        print("R*",end='')
                        break
                    else:
                        current = current.right
                        print("R",end='')
            print()
    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)