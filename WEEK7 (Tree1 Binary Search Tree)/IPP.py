class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    current = current.right
        return self.root

    def max(self):
        if self.root is None:
            return
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

    def min(self):
        if self.root is None:
            return
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.data

    def multi(self, k, multiplier):  # bfs then multiply
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            curr = q.dequeue()
            if curr.data > k:
                curr.data = curr.data*multiplier
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)

    def BFS(self):
        if self.root is None:
            return "Empty Tree"
        q = Queue()
        q.enqueue(self.root)
        output = "Breadth : "
        while not q.is_empty():
            current = q.dequeue()
            output += str(current.data) + ' '
            if current.left is not None:
                q.enqueue(current.left)
            if current.right is not None:
                q.enqueue(current.right)
        return output

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)


pre = 'Preorder : '
post = 'Postorder : '
ino = 'Inorder : '


def preorder(curr):
    global pre
    if curr is not None:
        pre += str(curr.data) + ' '
        preorder(curr.left)
        preorder(curr.right)


def inorder(curr):
    global ino
    if curr is not None:
        inorder(curr.left)
        ino += str(curr.data) + ' '
        inorder(curr.right)


def postorder(curr):
    global post
    if curr is not None:
        postorder(curr.left)
        postorder(curr.right)
        post += str(curr.data)+' '

T = BST()
inp = list(map(int, input('Enter Input : ').split()))
for item in inp:
    root = T.insert(item)
preorder(T.root)
print(pre)
inorder(T.root)
print(ino)
postorder(T.root)
print(post)
print(T.BFS())