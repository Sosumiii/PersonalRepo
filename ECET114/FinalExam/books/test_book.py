#Elvis Nguyen
from books import book
import pickle

def main():
    book1 = book("Get Started with Python", 66.99, 100)
    book2 = book("Get Started with Visual Basic", 55.99, 88)

    print(book1.getQuantity())
    book1.sellCopies(10)
    print(book1.getQuantity())

    outfile = open("bookInfo.dat", "wb")
    pickle.dump(book1, outfile)
    pickle.dump(book2, outfile)

    outfile.close()

    infile = open("bookInfo.dat", "rb")
    endOfFile = False
    while not endOfFile:
        try:
            phone = pickle.load(infile)
            print(phone)
            
        except EOFError:
            endOfFile = True

if __name__ == "__main__":
    main()