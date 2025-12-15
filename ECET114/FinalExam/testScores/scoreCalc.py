#Elvis Nguyen

def main():
    infile = open("test_scores.csv", "r")
    lines = infile.readlines()
    infile.close()

    lineCounter = 0
    scoreInstanceCounter = 0
    finalTotal = 0

    for line in lines:
        nums = line.split(",")
        lineCounter += 1

        total = 0
        for num in nums:
            total += int(num)
            scoreInstanceCounter += 1

        print(f"\nTotal score in line {lineCounter}: {total}")
        print(f"Average score in line {lineCounter}: {total/len(nums)}\n")

        finalTotal += total

    print(f"Final score total for the entire file: {finalTotal}. Average for all of the scores in the file: {finalTotal/scoreInstanceCounter:.2f}")

if __name__ == "__main__":
    main()        
