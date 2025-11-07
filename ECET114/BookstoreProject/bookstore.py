from Books import booksModifier

def main():
    #Create the list of books
    booksMod = booksModifier()
    keepGoing = "y"
    #booksMod.getAllInfo()
    booksMod.setQuantity("dingus 1", 860)
    #while (keepGoing == "y"):
    """ booksMod.addBook() """
    #    keepGoing = input("Would you like to keep going? (y/n): ").lower()

    booksMod.closeFile()

if __name__ == "__main__":
    main()