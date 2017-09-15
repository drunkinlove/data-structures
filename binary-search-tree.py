class Node:
    """
    The node class, which we will spawn the tree with.
    The key principle of binary trees is that, at any given moment,
    the right child of a node is larger than it, and the left child is
    always smaller.
    (This is only true if tree's order relation is a total order.
    Which it is, because the tree is constructed that way by the program,
    and not provided in advance by some jerk who just had to screw it up.

    Due to all of the algorithms being implemented as methods, if we want
    to perform an algorithm on the whole tree, 
    we should invoke the method on the root.
    """

    def __init__(self, value):
        """
        Node constructor.
        Each node instance contains three attributes: link to its left and
        right children, and its value.
        """
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        """
        Insert a new node with specified value.
        """
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def search(self, value):
        """
        Iterative search in the (sub)tree for the node with specified value,
        from the node to the bottom of the tree.
        """
        current_node = self
        while current_node != None:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def childrencount(self, value):
        """
        Returns the number of children of the node with specified value.
        """
        cnt = 0
        node = self.search(value)
        if node.left: # if it exists
            cnt += 1
        if node.right:
            cnt += 1
        return cnt

    def findmin(self):
        """
        Returns node with smallest value in the (sub)tree.
        """
        current_node = self
        while current_node.left: #while it exists
            current_node = current_node.left
        return current_node

    def lookforparent(self, value, parent=None):
        """
        Iterative search, with a slightly different output.
        """
        if value < self.value:
            if self.left is None:
                return None
            return self.left.lookforparent(value, self)
            # We enter the cycle again, but now we have moved one element
            # down our tree. And there must be a parent now,
            # so we cyclically set the parent variable to the node that we
            # just passed by.
            # Note that if the node we invoke the method on had the same
            # value as the one we were searching for, the parent=None
            # attribute would've played its role and we naturally
            # would have gotten None as the output.
        elif value > self.value:
            if self.right is None:
                return None
            return self.right.lookforparent(value, self)
        else:
            return parent

    def delete(self, value):
        """
        Delete node in the (sub)tree containing specified value.
        """
        node, parent = self.search(value), self.lookforparent(value)
        if node is not None:
            if self.childrencount(node.value) == 0: 
            # if node has no children, just remove it
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                    del node
                else:
                    self.value = None
            elif self.childrencount(node.value) == 1:
                # if node has 1 child, replace node with its child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                    del node
                else:
                    self.left = n.left
                    self.right = n.right
                    self.value = n.value
            else:
                # if node has 2 children, replace it with the next bigger node
                # look to the right first, then pick the leftmost node
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # found it. now replace node value with its successor's value
                node.value = successor.value
                # fix the old node that we have now moved
                if parent.left == successor: 
                    # if there actually was a node to the left of the one to
                    # the right to the one we're removing...
                    parent.left = successor.right
                else:
                    # else, if we could not find any nodes to the left of the 
                    # one to the right of the one we're removing...
                    # meaning, the child of the node being removed only has
                    # children to the right. 
                    # THEN, we replace the removed node with the one to the
                    # right, essentially moving the branch up by an element.
                    parent.right = successor.right

    def traverse(self):
        """
        Print tree contents in order.
        Due to the arranged structure of the tree, the algorithm for this
        is quite simple.
        """
        if self.left: # if there's anything to the left
            self.left.traverse()
        print(self.value)
        if self.right:
            self.right.traverse()

    def searchRecursively(self, value):
        """
        Recursive search for the node with specified value.
        """
        if self is None or self.value == value:
            # if there is no (sub)tree, or we have found the node, stop this madness
            return self
        if value < self.value:
            return self.left.searchRecursively(value)
        else: 
            return self.right.searchRecursively(value)

    def __str__(self):
        """
        A method to print info about a node. 
        """
        if self.childrencount(self.value) == 0:
            return("A node with value %s." % str(self.value))
        if self.left != None and self.right != None:
            return("A node with value %s. Its left child is a node with value"
                " %s, and the right child is a node with value %s."
                % (str(self.value), str(self.left.value),
                str(self.right.value)))
        elif self.left == None:
            return("A node with value %s. Its right child is a node with"
                " value %s."  % (str(self.value),
                str(self.right.value)))
        else:
            return("A node with value %s. Its left child is a node with value" 
                " %s."  % (str(self.value),
                str(self.left.value)))


root = Node(int(input("First, let's create the tree. Enter the root:\n")))
root.insert(int(input("Another one:\n")))
root.insert(int(input("One more:\n")))
root.insert(int(input("Final one:\n")))
print("\nThis is what our binary tree currently contains:")
root.traverse()
print("\nNow, let's look up info about an element.")
inf = int(input("Enter a value that corresponds to a node: \n"))
print(root.search(inf))
print("\nIts parent is: \n" + str(root.lookforparent(inf)))
todelete = root.search(int(input("Now, let's delete a node. Input the "
    "corresponding value:\n")))
print("\nBye-bye, " + str(todelete.value) + "!\n")
children = root.childrencount(todelete.value)
root.delete(todelete.value)
if children != 0:
    print("Its place was taken by one of its children.")
else:
    print("It's gone for good!")
input("\nNow press Enter to see what's left.\n")
print("These are the elements left in the tree:")
root.traverse()
input()
input("Whew.\n")
print("Alright, that's enough playing with binary trees. Please feel free to"
    " return to your daily duties. Thank you for attention!")