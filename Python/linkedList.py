import csv
from finalMain import hashnum

class LinkedList:

    global TBArray
    TBArray = [None] * 7

    #-------------Handles Insertion for Hash Table-----------------
    def add(self, entry, index):
        global TBArray
        if TBArray[index] is None:
            TBArray[index] = entry
        else:
            firstNode = TBArray[index]
            entry.setNext(firstNode)
            TBArray[index] = entry

    #-------------Handles Retrieval for Hash Table-----------------
    def get(self, name, index):
        if TBArray[index] is None:
            return None
        else:
            entry = TBArray[index]
            while entry is not None and entry.getName() != name:
                entry = entry.getNext()

            return entry

    #-------------Handles Deletion for Hash Table-----------------
    def remove(self, name, index):
        global TBArray
        if TBArray[index] is not None:
            prev = None
            entry = TBArray[index]
            while entry.getNext is not None and entry.getName() != name:
                prev = entry
                entry = entry.getNext()

            if entry.getName() == name:
                if prev is None:
                    TBArray[index] = entry.getNext()
                else:
                    prev.setNext(entry.getNext())
            else:
                return None
            return entry
        return None

    #-------------Handles Displaying Hash Table contents-----------------
    def display(self, index):
        npointer = TBArray[index]
        while npointer is not None:
            print(npointer.name + ", " + npointer.address + ", " + npointer.number + " => "),
            npointer = npointer.getNext()
        print("null"),

    #-------------Handles printing Hash Table contents to output file-----------------
    def printContents(self):
        c = csv.writer(open("C:/eclipse/java-oxygen2/eclipse/workspace/FinalProject/src/output-file.csv", "wb"))
        for index in range(hashnum):
            npointer = TBArray[index]
            while npointer is not None:
                c.writerow([npointer.name, npointer.address, npointer.number])
                npointer = npointer.getNext()
