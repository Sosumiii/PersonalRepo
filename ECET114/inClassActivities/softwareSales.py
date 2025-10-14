#Elvis Nguyen
#Software Sales

run = True #only used for testing purposes
pkgPrice = 99.00

while (run):
    numOfPkgs = int(input("How many packages do you intend to purchase? "))
    
    while (numOfPkgs < 0):
        print(("Invalid response."))
        numOfPkgs = int(input("How many packages do you intend to purchase? "))

    if (numOfPkgs >= 10 and numOfPkgs <= 19):
        discount = 0.9 #10% off
        dspDiscount = "10%"
    elif (numOfPkgs >= 20 and numOfPkgs <= 49):
        discount = 0.8 #20% off
        dspDiscount = "20%"
    elif (numOfPkgs >= 50 and numOfPkgs <= 99):
        discount = 0.7 #30% off
        dspDiscount = "30%"
    elif (numOfPkgs >= 100):
        discount = 0.6 #40% off
        dspDiscount = "40%"
    else:
        discount = 1 #No discount
        dspDiscount = "0%"

    total = (numOfPkgs * pkgPrice) * discount
    print(f"You have chosen to purchase {numOfPkgs} software packages. Your total discount is {dspDiscount} and your total with the discounts is ${total:.2f}. ")

    reRun = input("Would you like to run this program again? Y/n: ").lower()

    if (reRun == "n"):
        run = False