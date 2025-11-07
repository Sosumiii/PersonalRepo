#Elvis Nguyen
#Falling Distance Calculator Program

def distanceCalc(time:float):
    gravity = 9.8
    result = ((time**2) * gravity)/2

    return result

def main():
    fallTime = float(input("Enter how long the fall was (use decimal points): "))
    distance = distanceCalc(fallTime)

    print(f"Your object fell {distance:.2f} meters.")

main()
