import sys
n = int(input("Enter the size of the graph --> "))

g = []
v = []
c = []
d = []

print("\nEnter the graph")
for i in range(n):
    temp = list(map(int, input().split()))
    g.append(temp)
    v.append(0)
    c.append(0)
    d.append(0)

x = n - 1
v[x] = x
c[x] = 0
d[x] = x
while (x > 0):
    x -= 1
    min = sys.maxsize

    for i in range(n):
        if g[x][i] != 0 and (g[x][i] + c[i]) < min:
            min = g[x][i] + c[i]
            index = i
    v[x] = x
    c[x] = min
    d[x] = index

t = 0
path = ""
while t != n - 1:
    path += str(v[t]+1) + " - "
    t = d[t]

print("Shortest Path is: " + path + str(t+1))
print("Minimum cost is:", c[0])