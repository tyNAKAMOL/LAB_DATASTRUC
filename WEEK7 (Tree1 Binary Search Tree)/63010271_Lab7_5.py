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
    
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def checkpos(self,node,data):
        output = ""
        if node !=None:
            if node.data == data:
                if node==self.root:return "root"
                elif node.left != None or node.right != None:return "Inner"
                else:return "Leaf"
            output = self.checkpos(node.left,data)
            output = self.checkpos(node.right,data)
            return output


    # def checkpos(self,x):
    #     output = ""
    #     current = self.root
    #     if current.data==x:output="Root"
    #     else:
    #         while current:
    #             if x <= current.data:
    #                 if x == current.data:
    #                     if current.left != None or current.right != None:
    #                         output="Inner"
    #                     else:
    #                         output="Leaf"
    #                     break
    #                 else:
    #                     current = current.left
    #             else:
    #                 if x == current.data:
    #                     if current.left != None or current.right != None:
    #                         output="Inner"
    #                     else:
    #                         output="Leaf"
    #                     break
    #                 else:
    #                     current = current.right
    #         if output=="":output="Not exist"
    #     return print(output)
    
    def checkpos(self,node,data):
        output = ""
        if node !=None:
            if node.data == data:
                if node==self.root:return "root"
                elif node.left != None or node.right != None:return "Inner"
                else:return "Leaf"
            output = self.checkpos(node.left,data)
            output = self.checkpos(node.right,data)
            return output


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
print(T.checkpos(root,inp[0])) if T.checkpos(root,inp[0]) != None else print("Not exist")