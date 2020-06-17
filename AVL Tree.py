# AVL tree - Self Balancing Tree
# Operations - Insertion and Deletion

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0 # Height of a single node is 0

class AVL:
    def __init__(self):
        self.root = None
        self.start = '\033[93m'
        self.end = '\033[00m'

    def Insert(self, node):
        self.root = self._Insert(self.root, node)

    # Step 1: Insert Node
    def _Insert(self, root, node):
        if root is None:
            return Node(node)
        elif node < root.data:
            root.left = self._Insert(root.left, node)
        elif node > root.data:
            root.right = self._Insert(root.right, node)

        # Step 2: Update the heights of the node right from inserted node to root node
        # Because first the height of the inserted node will be updated then its parent height and so on...(Visualize Recursion)
        root.height = 1 + max(self.GetHeight(root.left), self.GetHeight(root.right))

        # Step 3: Get the balance factor of the node
        BalanceFactor = self.GetBalanceFactor(root)

        # Step 4: Perform Rotations
        # After getting balance factor there will be 4 cases

        # Case 1: Left
        if BalanceFactor > 1 and node < root.left.data:
            return self.RightRotate(root)
        # Case 2: Right
        if BalanceFactor < -1 and node > root.right.data:
            return self.LeftRotate(root)
        # Case 3: Left - Right
        if BalanceFactor > 1 and node > root.left.data:
            root.left = self.LeftRotate(root.left)
            return self.RightRotate(root)
        # Case 4: Right - Left
        if BalanceFactor < -1 and node < root.right.data:
            root.right = self.RightRotate(root.right)
            return self.LeftRotate(root)

        # Used when no rotations are performed it return the original root
        return root

    def Delete(self, key):
        if self.root is None:
            print("Tree is empty!")
        else:
            self.root = self._Delete(self.root, key)

    def _Delete(self, root, key):
        if root is None:
            return None
        elif key < root.data:
            root.left = self._Delete(root.left, key)
        elif key > root.data:
            root.right = self._Delete(root.right, key)
        else:   # We found a match
            # case 1: the node is a leaf node
            if root.left is None and root.right is None:
                return None
            # case 2: the node has 1 children
            elif root.left is None and root.right is not None:
                return root.right
            elif root.right is None and root.left is not None:
                return root.left
            # Case 3: the node has 2 children
            # Then we find the in-order successor of that node and replace it
            else:
                x = root.left
                y = root.right
                if root.right.left is None:
                    root.right.left = x
                    return root.right
                else:
                    z = self.InOrderSuccessor(root.right)
                    z.left = x
                    z.right = y

                    # Update heights
                    z.right.height = 1 + max(self.GetHeight(z.right.left), self.GetHeight(z.right.right))
                    z.height = 1 + max(self.GetHeight(z.left), self.GetHeight(z.right))

                    return z

        # Step 2: Update the heights of the node right from inserted node to root node
        # Because first the height of the inserted node will be updated then its parent height and so on...(Visualize Recursion)
        root.height = 1 + max(self.GetHeight(root.left), self.GetHeight(root.right))

        # Step 3: Get the balance factor of the node
        BalanceFactor = self.GetBalanceFactor(root)

        # Step 4: Perform Rotations
        # After getting balance factor there will be 4 cases

        # Case 1: Left - Heavy only on left
        if BalanceFactor > 1 and self.GetBalanceFactor(root.left) >= 0:
            return self.RightRotate(root)
        # Case 2: Right - Heavy only of right
        if BalanceFactor < -1 and self.GetBalanceFactor(root.right) < 0:
            return self.LeftRotate(root)
        # Case 3: Left - Right - Heavy on left-right
        if BalanceFactor > 1 and self.GetBalanceFactor(root.left) < 0:
            root.left = self.LeftRotate(root.left)
            return self.RightRotate(root)
        # Case 4: Right - Left - Heavy on right - left
        if BalanceFactor < -1 and self.GetBalanceFactor(root.right) >= 0:
            root.right = self.RightRotate(root.right)
            return self.LeftRotate(root)

        # Used when no rotations are performed it return the original root
        return root

    def LeftRotate(self, oldRoot):
        newRoot = oldRoot.right
        temp = newRoot.left

        # Perform Rotations
        newRoot.left = oldRoot
        oldRoot.right = temp

        # Update the heights of old and new roots
        oldRoot.height = 1 + max(self.GetHeight(oldRoot.left), self.GetHeight(oldRoot.right))
        newRoot.height = 1 + max(self.GetHeight(newRoot.left), self.GetHeight(newRoot.right))

        # Return the new root
        return newRoot

    def RightRotate(self, oldRoot):
        newRoot = oldRoot.left
        temp = newRoot.right

        # Perform Rotations
        newRoot.right = oldRoot
        oldRoot.left = temp

        # Update the heights of old and new roots
        oldRoot.height = 1 + max(self.GetHeight(oldRoot.left), self.GetHeight(oldRoot.right))
        newRoot.height = 1 + max(self.GetHeight(newRoot.left), self.GetHeight(newRoot.right))

        # return the new root
        return newRoot

    def GetHeight(self, node):
        if node is None:
            return -1   # Height of a empty node is -1
        return node.height  # If the node is not empty the return the height associated with that node

    def GetBalanceFactor(self, node):
        if node is None:
            return 0
        return self.GetHeight(node.left) - self.GetHeight(node.right)

    def InOrderSuccessor(self, currentNode):
        while currentNode.left != None:
            parent = currentNode
            currentNode = currentNode.left
        parent.left = None
        return currentNode

    def PreOrder(self):
        if self.root is None:
            print("The tree is empty!")
        else:
            self._PreOrder(self.root)

    def _PreOrder(self, node):
        if node is not None:
            print(self.start + str(node.data) + self.end, end = " ")
            self._PreOrder(node.left)
            self._PreOrder(node.right)

avlTree = AVL()

while True:
    print("\nEnter 1 to insert a node into the tree")
    print("Enter 2 to delete a node from the tree")
    print("Enter 3 to view the tree")
    print("Enter 4 to quit")

    UserChoice = int(input("Your Choice >> "))

    if UserChoice is 1:
        node = int(input("Enter node to insert >> "))
        avlTree.Insert(node)

    if UserChoice is 2:
        node = int(input("Which node do you want to delete? >> "))
        avlTree.Delete(node)

    if UserChoice is 3:
        avlTree.PreOrder()

    if UserChoice is 4:
        quit()