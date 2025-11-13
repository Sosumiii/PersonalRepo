from Books import booksModifier

def main():
    #Create the list of books
    booksMod = booksModifier()
    keepGoing = "y"

    while True:
        print("\n")
        print("Elvis's Bookstore")
        print("-----------------------")
        print("1. Create a list of books")
        print("2. Display all books")
        print("3. Add a new book")
        print("4. Search a book")
        print("5. Change the quantity of a book")
        print("6. Remove a book")
        print("7. Quit the program")

        answer = int(input("Please a number selection from the list above (ex: type '1' if you want to create a list of books): "))
        match answer:
            case 1:
                booksMod.addBook()

            case 2:
                booksMod.getAllInfo()

            case 3:
                booksMod.addBook()

            case 4:
                title = str(input("Please enter the title of the book that you are searching for: "))
                booksMod.getBook(title)

            case 5:
                title = str(input("Please enter the title of the book that you are searching for: "))
                quantity = int(input("Please enter the new quantity of the book: "))
                booksMod.setQuantity(title, quantity)

            case 6:
                title = str(input("Please enter the title of the book that you want to remove: "))
                booksMod.removeBook(title)

            case 7:
                print("Exiting program")
                break

            case _:
                print("-----------------------")
                print("Invalid Choice")
                print("-----------------------")



if __name__ == "__main__":
    main()