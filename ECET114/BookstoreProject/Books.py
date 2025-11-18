import os
fileName = "books.txt"

class Books():
    def __init__(self):
        super().__init__()

    def addSingularBook(self):
        self.bookFile = open(fileName, "a")
        title = input("Enter the title of the book: ")
        price = float(input("Enter the price of the book: $"))
        quantity = int(input("Enter the amount of books: "))

        self.bookFile.write(title + "\n")
        self.bookFile.write(f"{price:.2f}\n")
        self.bookFile.write(str(quantity) + "\n")

        self.closeFile()

    def addBook(self):
        self.bookFile = open(fileName, "w")

        while True:
            print("\n")
            
            title = input("Enter the title of the book: ")
            price = float(input("Enter the price of the book: $"))
            quantity = int(input("Enter the amount of books: "))

            self.bookFile.write(title + "\n")
            self.bookFile.write(f"{price:.2f}\n")
            self.bookFile.write(str(quantity) + "\n")

            keepGoing = input("Would you like to keep adding books? (y/n): ").lower()

            if (keepGoing != "y"):
                break
    
        self.closeFile()

    def getAllInfo(self):
        print("\n")
        self.bookFile = open(fileName, "r")
        bookTitle = self.bookFile.readline()

        while (bookTitle != ""):
            bookTitle = bookTitle.rstrip("\n")
            price = float(self.bookFile.readline())
            quantity = int(self.bookFile.readline())
            print(f"Title: {bookTitle}")
            print(f"Price: {price:.2f}")
            print(f"Quantity: {quantity}\n")
            bookTitle = self.bookFile.readline()

        self.closeFile()

    def closeFile(self):
        self.bookFile.close()

    def getBook(self, title: str):
        print("\n")

        found = False
        self.bookFile = open(fileName, "r")
        bookTitle = self.bookFile.readline()

        while (bookTitle != ""):
            bookTitle = bookTitle.rstrip("\n")
            price = float(self.bookFile.readline())
            quantity = int(self.bookFile.readline())
            
            if (bookTitle.lower() == title.lower()):
                print(f"Title: {bookTitle}")
                print(f"Price: {price:.2f}")
                print(f"Quantity: {quantity}\n")
                found = True

            bookTitle = self.bookFile.readline()
        
        if (found == False):
            print("Book was not found.")

        self.closeFile()


    def setQuantity(self, title: str, quantityChange: int):
        print("\n")

        self.bookFile = open(fileName, "r")
        tempFile = open("tempBooks.txt", "a")
        
        bookTitle = self.bookFile.readline()
        while (bookTitle != ""):
            bookTitle = bookTitle.rstrip("\n")
            price = float(self.bookFile.readline())
            quantity = int(self.bookFile.readline())
            
            if (bookTitle.lower() == title.lower()):
                found = True
                tempFile.write(f"{bookTitle}\n")
                tempFile.write(f"{price:.2f}\n")
                tempFile.write(str(quantityChange) + "\n")

            else:
                tempFile.write(f"{bookTitle}\n")
                tempFile.write(f"{price:.2f}\n")
                tempFile.write(str(quantity) + "\n")

            bookTitle = self.bookFile.readline()

        tempFile.close()
        self.closeFile()

        os.remove("books.txt")
        os.rename("tempBooks.txt", "books.txt")
        
        if not found:
            print("Book was not found.")

        else:
            print(f"The quantity for {title} has been updated to {quantityChange}.")

    def removeBook(self, title: str):
        print("\n")

        self.bookFile = open(fileName, "r")
        tempFile = open("tempBooks.txt", "a")
        
        bookTitle = self.bookFile.readline()
        while (bookTitle != ""):
            bookTitle = bookTitle.rstrip("\n")
            price = float(self.bookFile.readline())
            quantity = int(self.bookFile.readline())
            
            if (bookTitle.lower() == title.lower()):
                found = True

            else:
                tempFile.write(f"{bookTitle}\n")
                tempFile.write(f"{price:.2f}\n")
                tempFile.write(str(quantity) + "\n")

            bookTitle = self.bookFile.readline()

        tempFile.close()
        self.closeFile()

        os.remove("books.txt")
        os.rename("tempBooks.txt", "books.txt")
        
        if not found:
            print("Book was not found.")

        else:
            print(f"{title} has been removed.")
