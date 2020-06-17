import sys
n = int(input("Enter the size of the graph --> "))
g = []
a = []

for i in range(n):
    inp = list(map(int, input().split()))
    g.append(inp)

min = sys.maxsize   # Integer with maximum value

# Our First task is to find the edges with with minimum value.
# And add the vertices into the checked vertices list(a)
for i in range(n):
    for j in range(n):
        if i != j and g[i][j] != 0:
            if g[i][j] < min:
                min = g[i][j]
                start = i
                end = j
a.append(start)
a.append(end)                
print()
print(a[0]+1, "-", a[1]+1, "-->", min) # Print 1st edge and its cost
total = min

for i in range(n-2):    # 1 edge is already printed now n-2 edges are remaining, because for n vertices we can have n-1 edges
    min = sys.maxsize
    for j in a: # Find the minimum edges from the vertices in the checked vertices list(a)
        for k in range(n):
            if k not in a and g[j][k] != 0: # vertex should not point to checked vertex because that will form a loop
                if g[j][k] < min:   # If you find the minimum cost
                    min = g[j][k]   # Store its cost
                    start = j       # Store its starting vertex
                    end = k         # Store its ending vertex
    total += min
    print(start+1, "-", end+1, "-->", min)
    a.append(end)   # Add the vertex to checked vertices list(a)
print("Minimum Cost:", total)