score = int(input("Enter the score "))

""" result = num % 2
if result == 0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.") """

if (score >= 90):
    print("A")
elif (score >= 80):
    print("B")
elif (score >= 70):
    print("C")
elif (score >= 60):
    print("D")
else:
    print("F")