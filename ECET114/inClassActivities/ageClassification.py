#Elvis Nguyen
#Age Classification

run = True

while (run):
    age = int(input("Enter your age: "))
    
    while (age < 0):
        print("Invalid response")
        age = int(input("Enter your age: "))

    if (age <= 1):
        print("Infant")
    elif (age > 1 and age < 13):
        print("Child")
    elif (age >= 13 and age < 20):
        print("Teenager")
    elif (age >= 20):
        print("Adult")

    reRun = str(input("Would you like to enter a different age? Y/n ").lower())
    if (reRun == "n"):
        run = False


