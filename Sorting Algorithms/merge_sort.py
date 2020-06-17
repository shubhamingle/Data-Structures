def Merge(left, right, a):
    i = 0
    j = 0
    k = 0
    LeftLength = len(left)
    RightLength = len(right)
    while i < LeftLength and j < RightLength:
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
            k += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1
    while i < LeftLength:
        a[k] = left[i]
        k += 1
        i += 1
    while j < RightLength:
        a[k] = right[j]
        k += 1
        j += 1

def MergeSort(a):
    if len(a) == 1:
        return a[0]
    left = []
    right = []
    mid = int(len(a) / 2)
    for i in range(mid):
        left.append(a[i])
    for i in range(mid, len(a)):
        right.append(a[i])
    MergeSort(left)
    MergeSort(right)
    Merge(left, right, a)

a = list(map(int, input().split()))
MergeSort(a)

print(a)