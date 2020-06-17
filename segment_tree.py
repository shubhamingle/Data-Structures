print("Enter array elements")
a = list(map(int, input().split()))
b = [0 for i in range(2*len(a))]

def SegmentTree(start, end, treeNode):
    if start == end:
        b[treeNode] = a[start]
        return

    mid = (start + end) // 2

    SegmentTree(start, mid, 2*treeNode)
    SegmentTree(mid+1, end, 2*treeNode+1)

    b[treeNode] = b[2*treeNode] + b[2*treeNode+1]

SegmentTree(0, len(a)-1, 1)
print(b)

print("To find the sum of numbers in given range")
x = int(input("Enter start index >> "))
y = int(input("Enter end index >> "))