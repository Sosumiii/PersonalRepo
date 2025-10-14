#Elvis Nguyen
#Feburary days

run = True

while (run):
    year = int(input("Enter a year: "))

    while (year <= 0):
        print("Invalid Reponse.")
        year = int(input("Enter a year: "))

    if (((year % 100 != 0) and (year % 4 == 0)) or (year % 400 == 0)):
        print("There are 29 days in February this year. It is a leap year.")
    
    else:
        print("There are 28 days in February this year. It is not a leap year.")

    reRun = input("Do you want to use this program again? Y/n: ").lower()

    if (reRun == "n"):
        run = False

            