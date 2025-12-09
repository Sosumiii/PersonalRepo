listOfNumbers = [5,9,16,345,12,1000,-1,5,6,2,8]

def compareNum(number: int):
    for i in range(len(listOfNumbers)):
        if (number < listOfNumbers[i]):
            print(f"The list number {listOfNumbers[i]} is greater than the list number {number}")
            
def main():
    numForComparison = int(input("Enter a number to compare to the list: "))
    compareNum(numForComparison)

if __name__ == "__main__":
    main()