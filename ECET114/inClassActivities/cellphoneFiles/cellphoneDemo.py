from cellphone import CellPhone
import pickle

def main():
    phone1 = CellPhone("Apple", "iPhone 17", 799.99)
    phone2 = CellPhone("Samsung", "Galaxy S25", 899.99)

    phone1.raisePrice(0.10)
    phone2.reducePrice(0.05)

    outfile = open("cellphone.dat", "wb")
    pickle.dump(phone1, outfile)
    pickle.dump(phone2, outfile)

    outfile.close()

    infile = open("cellphone.dat", "rb")
    endOfFile = False
    while not endOfFile:
        try:
            phone = pickle.load(infile)
            print(phone)
            
        except EOFError:
            endOfFile = True

if __name__ == "__main__":
    main()