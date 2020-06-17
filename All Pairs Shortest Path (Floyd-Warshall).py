import sys
n = int(input("Enter the size of the graph --> "))

g = []

print('\nEnter the graph')
for i in range(n):
    temp = list(map(int, input().split()))
    g.append(temp)

for i in range(n):
    for j in range(n):
        if i != j:
            if g[i][j] == 0:
                g[i][j] = sys.maxsize

for i in range(n):
    for j in range(n):
        if j != i:
            for k in range(n):
                if k != i and j != k:
                    if g[j][k] > g[j][i] + g[i][k]:
                        g[j][k] = g[j][i] + g[i][k]

for i in g:
    print(i)