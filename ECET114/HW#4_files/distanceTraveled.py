#Elvis Nguyen

def distanceCalculations(speed:int, hours:int):
    return speed * hours

speedInput = int(input("What was the speed you were traveling in mph? "))
timeInput = int(input("How long were you travelling in hours? "))

print("Hour         Distance")
print("---------------------")

for hours in range(timeInput):
    print((hours + 1), "          ", distanceCalculations(speedInput, (hours + 1)))