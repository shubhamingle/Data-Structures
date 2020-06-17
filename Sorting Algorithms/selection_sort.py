a = list(map(int, input().split()))

for i in range(len(a)-1):
    t = i
    for j in range(i+1, len(a)):
        if a[j] < a[t]:
            t = j
    temp = a[i]
    a[i] = a[t]
    a[t] = temp

print(a)