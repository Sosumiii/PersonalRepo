""" for num in range(0, 150, 5):
    print(f"hello, {num}") """

""" prod = 1

for num in range(1, 10+1):
    prod *= num

print(f"final result is {prod}") """
""" total = 0.0
MAX = 3
for counter in range(MAX):
    score = float(input("Enter the score: "))
    total += score

avg = total/MAX


print(f"{total:.2f}")
print(f"{avg:.2f}") """
total = 0
counter = 0
score = 0

while (score != -1):
    score = float(input("Enter the score: "))
    total += score

    counter += 1

avg  = total / counter

print(f"the total is {total}")
print(f"the average is {avg:.2f}")