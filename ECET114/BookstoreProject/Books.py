class booksModifier():
    def __init__(self):
        super().__init__()

    def addBook(self):
        self.bookFile = open("books.txt", "w")
        title = input("Enter the title of the book: ")
        price = float(input("Enter the price of the book: $"))
        quantity = int(input("Enter the amount of books: "))

        self.bookFile.write(title + "\n")
        self.bookFile.write(f"{price:.2f}\n")
        self.bookFile.write(str(quantity) + "\n")

    def getAllInfo(self):
        self.bookFile = open("books.txt", "r")
        bookTitle = self.bookFile.readline()
        while (bookTitle != ""):
            bookTitle = bookTitle.rstrip("\n")
            price = float(self.bookFile.readline())
            quantity = int(self.bookFile.readline())
            print(f"Title: {bookTitle}")
            print(f"Price: {price:.2f}")
            print(f"Quantity: {quantity}\n")
            bookTitle = self.bookFile.readline()

    def closeFile(self):
        self.bookFile.close()

    def getBook(self, title: str):
        self.bookFile = open("books.txt", "r")
        bookTitle = self.bookFile.readline()
        while True:
            bookTitle = bookTitle.rstrip()
            price = float(self.bookFile.readline())
            quantity = int(self.bookFile.readline())

            if (bookTitle.lower() == title.lower()):
                print(f"Title: {bookTitle}")
                print(f"Price: {price:.2f}")
                print(f"Quantity: {quantity}\n")
                break

            elif (bookTitle == ""):
                print("not found")
                break

            bookTitle = self.bookFile.readline()

    def setQuantity(self, title: str, quantityChange: int):
        self.bookFile = open("books.txt", "a+")
        self.bookFile.seek(0)
        while True:
            bookTitle = self.bookFile.readline()
            bookTitle = bookTitle.rstrip()
            price = float(self.bookFile.readline())
            quantity = int(self.bookFile.readline())

            if (bookTitle.lower() == title.lower()):
                self.bookFile.write(bookTitle + "\n")
                self.bookFile.write(f"{price:.2f}\n")
                self.bookFile.write(str(quantityChange) + "\n")
                break

    def removeBook(self):
        pass
