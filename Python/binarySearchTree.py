import csv
from finalMain import hashnum
from personNode import PersonNode

class BinarySearchTree:

    root = PersonNode()

    #-------------Handles Insertion for BST-----------------
    def add(self, entry, index):
        if self.root.name is None:
            self.root = entry
        else:
            nptr = self.root
            while nptr is not None:
                key = abs(hash(nptr.name)) % hashnum
                nptr_parent = nptr
                if key >= index:
                    nptr = nptr.leftChild
                    if nptr is None:
                        nptr_parent.leftChild = entry
                else:
                    nptr = nptr.rightChild
                    if nptr is None:
                        nptr_parent.rightChild = entry

    #-------------Handles Retrieval for BST-----------------
    def get(self, name, index):
        if self.root is None:
            return None
        nptr = self.root

        while nptr is not None:
            if name == nptr.name:
                return nptr
            else:
                key = abs(hash(nptr.name)) % hashnum
                if key >= index:
                    nptr = nptr.leftChild
                    if nptr is None:
                        return None
                else:
                    nptr = nptr.rightChild
                    if nptr is None:
                        return None
        return None

    #-------------Handles Deletion for BST-----------------
    def remove(self, name, index):
        nptr = self.root
        nptr_parent = self.root
        tracker = 0

        while nptr.getName() != name:
            nptr_parent = nptr
            key = abs(hash(nptr.getName())) % hashnum
            if key >= index:
                nptr = nptr.leftChild
                tracker = 1
            else:
                nptr = nptr.rightChild
                tracker = 0
            if nptr is None:
                return None

        #--------Case 1: If the node has no child---------
        if nptr.leftChild is None and nptr.rightChild is None:
            if nptr is self.root:
                self.root = None

            if tracker == 1:
                nptr_parent.leftChild = None
            else:
                nptr_parent.rightChild = None

        #----------Case 2: If the node has one child-----------
        elif nptr.leftChild is None:
            if nptr is self.root:
                self.root = nptr.rightChild

            if tracker == 1:
                nptr_parent.leftChild = nptr.rightChild
            else:
                nptr_parent.rightChild = nptr.rightChild

        elif nptr.rightChild is None:
            if nptr is self.root:
                self.root = nptr.leftChild

            if tracker == 1:
                nptr_parent.leftChild = nptr.leftChild
            else:
                nptr_parent.rightChild = nptr.leftChild

        #----------Case 3: If the node has two children----------
        else:
            successor = self.successor(nptr)
            print(successor.name)
            if nptr is self.root:
                self.root = successor
            elif tracker == 1:                          # This was a bug in the Java version! Was just an "if"
                nptr_parent.leftChild = successor
            else:
                nptr_parent.rightChild = successor

            successor.leftChild = nptr.leftChild
            if successor is not nptr.rightChild:
                successor.rightChild = nptr.rightChild

        return nptr

    #-------------Find successor of Node being deleted-----------------
    def successor(self, x):
        nptr_parent = None
        nptr = None
        temp = x.rightChild

        while temp is not None:
            nptr_parent = nptr
            nptr = temp
            temp = temp.leftChild

        if nptr is not x.rightChild:
            nptr_parent.leftChild = nptr.rightChild

        return nptr

    #-------------Handles displaying BST contents-----------------
    def display(self, node):
        if node is not None:
            self.display(node.leftChild)
            print(node.name + ", " + node.address + ", " + node.number + ", " + str(abs(hash(node.name)) % hashnum))
            self.display(node.rightChild)

    #-------------Sets up writing BST contents to output file-----------------
    def printContents(self, root):
        c = csv.writer(open("PATH_TO_'output-data.csv'_GOES_HERE", "wb"))
        self.output(root, c)

    #-------------Actually does the writing to output file-----------------
    def output(self, root, c):
        if root is not None:
            self.output(root.leftChild, c)
            c.writerow([root.name, root.address, root.number])
            self.output(root.rightChild, c)
