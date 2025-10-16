def calculateinterest(principal, rate, periods):
    return principal * rate * periods

def main():
    interest = calculateinterest(10000.0, 0.01, 10)
    print(f"The interest is {interest}")

main()