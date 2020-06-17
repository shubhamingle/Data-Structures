# Single Source Shortest Path for undirected graphs
import sys
g = []
w = []
a = []

n = int(input("Enter the size of the graph --> "))

print("Enter the graph\n")
for i in range(n):
    temp = list(map(int, input().split()))
    g.append(temp)
    w.append(sys.maxsize)

start = int(input("Enter the source --> "))
end = int(input("Enter the destination --> "))

if g[start][end] != 0:
    print("Shortest Path is:", g[start][end])
else:
    x = start
    w[x] = 0
    while x != end:
        min = sys.maxsize
        for j in range(n):
            if g[x][j] != 0 and j not in a:
                w[j] = g[x][j] + w[x]
        a.append(x)

        for i in range(n):
            if i not in a:
                if w[i] < min:
                    min = w[i]
                    x = i
path = ""
for i in a:
    path += str(i) + " - "

print("Path is: " + path + str(x))
print("Minimum cost is:", w[x])