a = list(map(int, input().split()))
n = len(a)

for i in range(1, n):
    value = a[i]
    c = i
    while c > 0 and a[c-1] > value:
        a[c] = a[c-1]
        c -= 1
    a[c] = value

print(a)