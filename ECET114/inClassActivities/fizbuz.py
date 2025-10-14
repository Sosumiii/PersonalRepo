counterFiz = 0
counterBuz = 0
counterFizBuz = 0

for x in range(1, 100+1):

    if (x % 3 == 0) and (x % 5 ==0):
        print(f"{x} is a fizbuz")
        counterFizBuz += 1
    
    elif (x % 3 == 0):
        print(f"{x} is a fizz")
        counterFiz += 1
    
    elif (x % 5 == 0):
        print(f"{x} is a buzz")
        counterBuz += 1

    else:
        print(x)

print(f"The number of fiz is {counterFiz}")
print(f"The number of buz is {counterBuz}")
print(f"The number of fizbuz is {counterFizBuz}")