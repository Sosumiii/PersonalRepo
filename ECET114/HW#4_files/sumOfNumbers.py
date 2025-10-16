#Elvis Nguyen

sum = 0
numInput = 0

while (numInput >= 0):
    sum += numInput
    numInput = int(input("Enter a positive number to add to the total sum. Enter a negative number to quit and display the sum: "))
    
print(sum)