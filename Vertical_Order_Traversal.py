class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.x = 0

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right =Node(8) 
root.right.right.left = Node(10) 
root.right.right.right = Node(9) 
root.right.right.left.right = Node(11) 
root.right.right.left.right.right = Node(12) 

'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.left.right = Node(8)
root.right.right = Node(7)
root.right.right.right = Node(9)
'''
min = 0
max = 0
start = '\033[93m'
end = '\033[00m'

def AssignNumber(parent, node, flag):
    global min, max
    if node is not None:
        if flag == 'Left':
            node.x = parent.x - 1
            parent = node 
            if node.x < min:
                min = node.x
        elif flag == 'Right':
            node.x = parent.x + 1
            parent = node
            if node.x > max:
                max = node.x
        AssignNumber(parent, parent.left, 'Left')
        AssignNumber(parent, parent.right, 'Right')
    return min, max

def PutInArray(node, min, max):
    if node is not None:
        if node.x < 0:
            a[node.x + abs(min)].append(node.data)
        elif node.x >= 0:
            a[node.x + abs(min)].append(node.data)
        PutInArray(node.right, min, max)    # Should put right before left for getting the correct top view
        PutInArray(node.left, min, max)

t = AssignNumber(root, root, None)
z = abs(t[0]) + t[1] + 1
a = [[] for i in range(z)]
PutInArray(root, t[0], t[1])

print(start + "Vertical Order Traversal of the tree is" + end)
for i in range(len(a)):
    temp = ""
    for j in range(len(a[i])):
        temp += str(a[i][j])  + " "
    print(temp)

print(start + "Top View of the tree is" + end)
for i in range(len(a)):
    print(a[i][0], end = " ")