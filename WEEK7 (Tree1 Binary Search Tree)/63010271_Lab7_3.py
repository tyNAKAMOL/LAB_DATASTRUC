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
        
    def LessThanorEqual(self,root,data):
        count = 0
        if root == None :
            return count
        count += self.LessThanorEqual(root.left,data)
        if root.data<=data:
            count+=1
        count += self.LessThanorEqual(root.right,data)
        return count

        
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
print("-"*50)
print("{}".format(T.LessThanorEqual(root,n)))