import math

def main():
    a = 3
    b = 4
    c = math.hypot(a, b)
    print(f"the result is {c}")

    r = 1

    area = math.pi * (r**2)
    print(f"The result is {area}")

    x = 30
    
    for x in range (0, 360+1):
        y = math.sin(math.radians(x))
        z = math.cos(math.radians(x))
        print(f"{x}\t{y:.2f}\t{z:.2f}")

main()