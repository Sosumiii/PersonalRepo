def main():
    infile=open("books.txt", "r")
    #print(type(infile))
    file_contents = infile.read()
    print(file_contents)
    infile.close()

if __name__ == "__main__":
    main()