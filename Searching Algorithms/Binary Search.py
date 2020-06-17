# For performing Binary Search we need the array to be sorted either in ascending or descending order
# We will make use of Quick Sort to sort the array in ascending order and then perform binary search on it

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

print("Enter array elements")
a = list(map(int, input().split()))
QuickSort(a, 0, len(a)-1)
'''
# Iterative Method
def BinarySearch(start, end, element):
    while start <= end:
        mid = (start + end) // 2    # you can also write start + (start - end) // 2 to avoid overflow. Since max size of integer is 2^31 - 1 for 32 bit processor
        if element == a[mid]:
            return mid
        elif element < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False
'''
# Recursive Method
def BinarySearch(start, end, element):
    mid = (start + end) // 2
    if element == a[mid]:
        return mid
    elif element < a[mid]:
        BinarySearch(start, mid-1, element)
    else:
        BinarySearch(mid+1, end, element)
    return False

print(a)

element = int(input("Enter element to search >> "))
found = BinarySearch(0, len(a)-1, element)
if found is False:
    print("{} not found!".format(element))
else:
    print("{} is present at index {}".format(element, found))