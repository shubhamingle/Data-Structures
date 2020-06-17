a = list(map(int, input().split()))

for i in range(len(a)):
    flag = 0
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            flag = 1
    if flag == 0:
        break

print(a)