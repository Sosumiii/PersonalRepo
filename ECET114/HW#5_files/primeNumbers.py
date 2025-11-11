#Elvis Nguyen  
#Prime Numbers
import math

def is_prime(value: int):
    if (value < 2):
        return False
    
    valueSqrt = int(math.sqrt(value))
    for i in range(2, valueSqrt+1):
        if ((value % i) == 0):
            return False
    return True
        
def main():
    keepGoing = True
    
    while (keepGoing == True):
        number = int(input("Enter a number to see if it is prime: "))
        prime = is_prime(number)

        if (prime == True):
            print(f"The number {number} is prime.")
        else:
            print(f"The number {number} is not prime.")

        loop = input("Would you like to keep going? (y/n): ").lower()

        if (loop == "n"):
            keepGoing = False

main()