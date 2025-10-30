def main():
    outfile = open("scores.txt", "w")
    for count in range(3):
        score = float(input("Enter the score:"))
        outfile.write(str(score)+"\n")

    outfile.close()

if __name__ == "__main__":
    main()