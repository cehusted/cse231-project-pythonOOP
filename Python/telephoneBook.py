from finalMain import hashnum
from linkedList import LinkedList
from binarySearchTree import BinarySearchTree
from personNode import PersonNode

class TelephoneBook:

    global linked, tree
    linked = LinkedList()
    tree = BinarySearchTree()

    #----------Handles insertion of a record into the hash table----------
    def insert(self, name, address, number):
        global linked
        index = abs(hash(name)) % hashnum
        if linked.get(name, index) is None:
            entry = PersonNode(name, address, number)
            linked.add(entry, index)
        else:
            updatePerson = linked.get(name, index)
            updatePerson.setAddress(address)
            updatePerson.setNumber(number)

    #----------Handles retrieval of a record from the hash table----------
    def retrieve(self, name):
        global linked
        index = abs(hash(name)) % hashnum
        return linked.get(name, index)

    # ----------Handles deletion of a record from the hash table----------
    def delete(self, name):
        global linked
        index = abs(hash(name)) % hashnum
        return linked.remove(name, index)

    #----------Displays the contents of the hash table----------
    def displayBook(self):
        for index in range(hashnum):
            print("\nTelephoneBook[" + str(index) + "] => "),
            linked.display(index)

    #----------Writes contents of hash table to output file----------
    def writeOutput(self):
        linked.printContents()

    '''
    ---------------------------------Methods for BST Below-----------------------------------------
    '''

    #----------Handles insertion of a record into the BST----------
    def bstInsert(self, name, address, number):
        global tree
        index = abs(hash(name)) % hashnum
        if tree.get(name, index) is None:
            entry = PersonNode(name, address, number)
            tree.add(entry, index)
        else:
            updatePerson = tree.get(name, index)
            updatePerson.setAddress(address)
            updatePerson.setNumber(number)

    #----------Handles retrieval of a record from the BST----------
    def bstRetrieve(self, name):
        index = abs(hash(name)) % hashnum
        return tree.get(name, index)

    #----------Handles deletion of a record from the BST----------
    def bstDelete(self, name):
        global tree
        index = abs(hash(name)) % hashnum
        return tree.remove(name, index)

    #----------Displays the entire BST contents----------
    def bstDisplayBook(self):
        print("-----------------------------------------")
        tree.display(tree.root)
        print("-----------------------------------------")

    #----------Writes contents of BST to output file----------
    def bstWriteOutput(self):
        tree.printContents(tree.root)
