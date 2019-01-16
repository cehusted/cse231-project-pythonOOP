class PersonNode:

    def __init__(self, name=None, address=None, number=None):
        self.number = number
        self.address = address
        self.name = name
        self.next = None
        self.rightChild = None
        self.leftChild = None

    #------------Returns the person's name------------
    def getName(self):
        return self.name

    #--------Returns the person's phone number--------
    def getTelephoneNumber(self):
        return self.number

    #----------Returns the person's address-----------
    def getAddress(self):
        return self.address

    #----------Returns the next person in the hash table----------
    def getNext(self):
        return self.next

    #----------Sets the next person (after this person) in the hash table----------
    def setNext(self, next):
        self.next = next

    #----------Sets the person's new address----------
    def setAddress(self, address):
        self.address = address

    #----------Sets the person's new address----------
    def setNumber(self, number):
        self.number = number