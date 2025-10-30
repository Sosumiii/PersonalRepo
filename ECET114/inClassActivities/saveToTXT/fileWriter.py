def main():
    outfile=open("books.txt", "w")
    outfile.write("Intro to Python 2\n")
    outfile.write("Calculus\n")
    outfile.write("English II\n")
    outfile.close()

if __name__ == "__main__":
    main()