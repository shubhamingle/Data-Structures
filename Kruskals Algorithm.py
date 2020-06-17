import sys
n = int(input("Enter the size of the graph --> "))
g = []
count = 0
total = 0
b = set()
c = set()  # Visited vertices

for i in range(n):
    temp = list(map(int, input().split()))
    g.append(temp)

a = [[] for i in range(n)]

flag = 0

def CheckLoop(x, y):
    global flag
    b.add(x)
    b.add(y)
    if y in a[x]:
        flag = 1
    else:
        for i in a[x]:
            if i not in b:
                CheckLoop(i, y)

# Our first task is to find the minimum
def FindMinimum():
    global count, flag, total
    min = sys.maxsize
    for i in range(n):
        for j in range(n):
            if g[i][j] not in c and g[i][j] != 0:
                if g[i][j] < min:
                    min = g[i][j]
                    start = i
                    end = j
    c.add(min)
    b.clear()
    loop = CheckLoop(start, end)
    if flag != 1:
    #if loop is not True:
        a[start].append(end)
        a[end].append(start)
        print(start+1, "-", end+1, "-->", min)
        total += min
        count += 1
    flag = 0

while count != n-1: # We will have n-1 edges in MST, where n is the number of vertices.
    FindMinimum()
print("Minimum cost:", total)