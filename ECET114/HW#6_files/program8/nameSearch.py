def convertFileIntoList(file):
    nameList = []
    inFile = open(file, "r")
    name = inFile.readline()

    while (name != ""):
        name = name.rstrip()
        name = name.lower()
        nameList.append(name)
        name = inFile.readline()

    inFile.close()
    return nameList

def isPopular(name: str, boysList, girlsList):
    name = name.lower()
    popularBoyName = False
    popularGirlName = False
    for i in range(len(boysList)):
        if (name == boysList[i]):
            popularBoyName = True

    for i in range(len(girlsList)):
        if (name == girlsList[i]):
            popularGirlName = True

    if popularBoyName:
        print(f"\nThe name {name} is a popular name for boys.\n")

    elif popularGirlName:
        print(f"\nThe name {name} is a popular name for girls.\n")
        
    else:
        print(f"\nThe name {name} was not a popular name.\n")

def main():
    boysNames = convertFileIntoList("BoyNames.txt")
    girlsNames = convertFileIntoList("GirlNames.txt")

    name = str(input("Please enter either a boyish or a girlish name to see if it was commonly used between 2000 and 2009: "))

    isPopular(name, boysNames, girlsNames)


if __name__ == "__main__":
    main()