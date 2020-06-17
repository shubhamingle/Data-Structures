def Partition(a, start, end):
    pivot = a[end]
    pIndex = start
    for i in range(start, end):
        if a[i] <= pivot:
            temp = a[i]
            a[i] = a[pIndex]
            a[pIndex] = temp
            pIndex += 1
    a[end] = a[pIndex]
    a[pIndex] = pivot
    return pIndex

def QuickSort(a, start, end):
    if start < end:
        pIndex = Partition(a, start, end)
        QuickSort(a, start, pIndex-1)
        QuickSort(a, pIndex+1, end)

a = list(map(int, input().split()))
QuickSort(a, 0, len(a)-1)
print(a)