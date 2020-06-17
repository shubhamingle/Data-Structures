import sys
n = int(input("Enter the size of the graph --> "))

g = []
w = []

for i in range(n):
    temp = list(map(int, input().split()))
    g.append(temp)
    w.append(sys.maxsize)

w[0] = 0
for i in range(n-1):
    for j in range(n):
        for k in range(n):
            if j !=k and g[j][k] != 0:
                if w[j] + g[j][k] < w[k]:
                    w[k] = w[j] + g[j][k]

print(w)
# Each value w(i) represents the minimum cost required from source(0) to ith vertex