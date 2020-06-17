n = int(input("Enter the size of the graph >> "))
g = []

for i in range(n):
    t = list(map(int, input().split()))
    g.append(t)

def BFSTraversal(x):
    q = []
    a = []
    q.append(x)
    a.append(x)
    while len(q) > 0:
        y = q[0]
        q.pop(0)
        for i in range(n):
            if g[y][i] != 0 and i not in a:
                q.append(i)
                a.append(i)
    return a

def DFSTraversal(x):
    s = []
    a = []
    s.append(x)
    a.append(x)
    while len(s) > 0:
        flag = 0
        y = s[len(s) - 1]
        for i in range(n):
            if g[y][i] != 0 and i not in a:
                s.append(i)
                a.append(i)
                flag = 1
                break
        if flag == 0:
            s.pop(len(s)-1)

    for i in range(len(a)):
        a[i] = str(a[i] + 1)

    path = " - ".join(a)
    return path

while True:
    print("Enter 1 for BFS Traversal")
    print("Enter 2 for DFS Traversal")
    print("Enter 3 to Quit")

    UserChoice = int(input("Your Choice >> "))

    if UserChoice is 1:
        StartVertex = int(input("Enter the starting StartVertex >> "))
        List = BFSTraversal(StartVertex)
        print(List)
    if UserChoice is 2:
        StartVertex = int(input("Enter the starting StartVertex >> "))
        List = DFSTraversal(StartVertex)
        print(List)
    if UserChoice is 3:
        quit()