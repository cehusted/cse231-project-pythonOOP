import csv

hashnum = 7

class FinalMain:

    # ---------Main method for running the hash table----------
    def hashTable(self):
        hashList = TelephoneBook()

        with open("PATH_TO_'input-data.csv'_GOES_HERE") as csvFile:
            data = csv.reader(csvFile)
            for row in data:
                name = row[0]
                address = row[1]
                number = row[2]
                hashList.insert(name, address, number)

        input = 0
        while input != 5:
            print("\nMenu for Hash Table")
            print("1. Insert Telephone Number\n2. Retrieve Telephone Number\n3. Delete Telephone Number\n4. Display Telephone Book\n5. End Program")
            try:
                input = int(raw_input("Enter choice (1-5): "))
            except ValueError:
                print("\nError: Please enter a valid number between 1 and 5")
                pass

            if input == 1:
                insertName = raw_input("\nPlease enter your name: ")
                insertAddress = raw_input("Please enter your address: ")
                insertNumber = raw_input("Please enter your phone number (e.g. 123-456-7890): ")
                hashList.insert(insertName, insertAddress, insertNumber)
                print("\nThe telephone book has been updated with this record")

            elif input == 2:
                retrievePerson = raw_input("\nEnter person's name: ")
                retrieved = hashList.retrieve(retrievePerson)
                if retrieved is None:
                    print("\n" + retrievePerson + " does not exist in the telephone book")
                else:
                    print(retrieved.name + "'s address is: " + retrieved.address)
                    print(retrieved.name + "'s telephone number is: " + retrieved.number)

            elif input == 3:
                deletePerson = raw_input("\nEnter person's name: ")
                deleted = hashList.delete(deletePerson)
                if deleted is None:
                    print("\n" + deletePerson + " does not exist in the telephone book")
                else:
                    print("Deleting: " + deleted.name + " (" + deleted.address + ") " + deleted.number)

            elif input == 4:
                print("\nDisplay Table")
                hashList.displayBook()
                print('')

            elif input == 5:
                hashList.writeOutput()
                print("\nData has been written to excel file.")
                break

            else:
                print("\nError: Please enter a valid number between 1 and 5")

    # ---------Main method for running the BST----------
    def bst(self):
        bstList = TelephoneBook()

        with open("PATH_TO_'input-data.csv'_GOES_HERE") as csvFile:
            data = csv.reader(csvFile)
            for row in data:
                name = row[0]
                address = row[1]
                number = row[2]
                bstList.bstInsert(name, address, number)

        input = 0
        while input != 5:
            print("\nMenu for Binary Search Tree")
            print("1. Insert Telephone Number\n2. Retrieve Telephone Number\n3. Delete Telephone Number\n4. Display Telephone Book\n5. End Program")
            try:
                input = int(raw_input("Enter choice (1-5): "))
            except ValueError:
                print("\nError: Please enter a valid number between 1 and 5")
                pass

            if input == 1:
                insertName = raw_input("\nPlease enter your name: ")
                insertAddress = raw_input("Please enter your address: ")
                insertNumber = raw_input("Please enter your phone number (e.g. 123-456-7890): ")
                bstList.bstInsert(insertName, insertAddress, insertNumber)
                print("\nThe telephone book has been updated with this record")

            elif input == 2:
                retrievePerson = raw_input("\nEnter person's name: ")
                retrieved = bstList.bstRetrieve(retrievePerson)
                if retrieved is None:
                    print("\n" + retrievePerson + " does not exist in the telephone book")
                else:
                    print(retrieved.name + "'s address is: " + retrieved.address)
                    print(retrieved.name + "'s telephone number is: " + retrieved.number)

            elif input == 3:
                deletePerson = raw_input("\nEnter person's name: ")
                deleted = bstList.bstDelete(deletePerson)
                if deleted is None:
                    print("\n" + deletePerson + " does not exist in the telephone book")
                else:
                    print("Deleting: " + deleted.name + " (" + deleted.address + ") " + deleted.number)

            elif input == 4:
                print("\nDisplay Table")
                bstList.bstDisplayBook()
                print('')

            elif input == 5:
                bstList.bstWriteOutput()
                print("\nData has been written to excel file.")
                break

            else:
                print("\nError: Please enter a valid number between 1 and 5")

if __name__ == "__main__":
    from telephoneBook import TelephoneBook
    text = raw_input("1. Hash Table\n2. Binary Search Tree\n")
    main = FinalMain()
    if text == '1':
        main.hashTable()
    else:
        main.bst()

