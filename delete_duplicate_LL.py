class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        if head is None:
            return
        currentNode = head
        nextNode = currentNode.next
        while nextNode is not None:
            if currentNode.data != nextNode.data:
                currentNode.next = nextNode
                currentNode = nextNode
            nextNode = nextNode.next
        # Mark the end of the linked list by pointing to None
        currentNode.next = None
        return head

myList= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=myList.insert(head,data)    
head=myList.removeDuplicates(head)
myList.display(head); 