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
        else:
            current = self.root
            while current:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right
            return self.root
        
    def in_order(self,root):
        I = []
        if not root:
            return I
        I = self.in_order(root.left)
        I.append(root.data)
        I = I + self.in_order(root.right)
        return I
        

        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp,n = input('Enter Input : ').split("/")
n = int(n)
inp = [int(i) for i in inp.split()]
count = 0
for i in inp:
    root = T.insert(i)
T.printTree(root)
X = T.in_order(root)
for i in range(len(X)):
    if n >= X[i]:
        count += 1
print("-"*50)
print("{}".format(count))