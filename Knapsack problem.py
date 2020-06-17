n = int(input("Enter the size of the bag --> "))
print("Enter the profit of the objects")
p = list(map(float, input().split()))
print("Enter the weight of the objects")
w = list(map(float, input().split()))

a = []
cost = 0
for i in range(len(p)):
    a.append(p[i] / w[i])

for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

            temp = p[i]
            p[i] = p[j]
            p[j] = temp

            temp = w[i]
            w[i] = w[j]
            w[j] = temp

for i in range(len(a)):
    if w[i] <= n:
        cost += p[i]
        n -= w[i]
    elif n > 0:
        cost += (n/w[i]) * p[i]
        n -= w[i]

print("Maximum Profit --> {:.2f}".format(cost))

# For 0/1 Knapsack we have to use dynamic programming