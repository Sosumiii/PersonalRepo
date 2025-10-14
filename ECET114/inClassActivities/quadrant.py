#Elvis Nguyen Quadrant assignment
xCoordinate = int(input("Enter the X coordinate:"))
yCoordinate = int(input("Enter the Y coordinate:"))

if (xCoordinate > 0 and yCoordinate > 0):
    print(f"The coordinates ({xCoordinate}, {yCoordinate}) are in the first quadrant.")

elif (xCoordinate < 0 and yCoordinate > 0):
    print(f"The coordinates ({xCoordinate}, {yCoordinate}) are in the second quadrant.")

elif (xCoordinate < 0 and yCoordinate < 0):
    print(f"The coordinates ({xCoordinate}, {yCoordinate}) are in the third quadrant.")

elif (xCoordinate > 0 and yCoordinate < 0):
    print(f"The coordinates ({xCoordinate}, {yCoordinate}) are in the fourth quadrant.")

else:
    print(f"The coordinates ({xCoordinate}, {yCoordinate}) are in the origin.")

""" 
if (xCoordinate >= 0):
    if (yCoordinate > 0):
        print("Quadrant I")
    elif (yCoordinate == 0):
        print("Origin")
    else:
        print("Quadrant IV")

else:
    if (yCoordinate > 0):
        print("Quadrant II")
    elif (yCoordinate < 0):
        print("Quadrant III")
 """