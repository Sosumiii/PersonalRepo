counter = 0
score = 0
total = 0

while (score != -1):
    counter += 1
    total += score

    if (score > 100) or (score < 0):
        print("Score is invalid")
        score = float(input("Enter the score: "))

    score = float(input("Enter the score: "))

if (counter != 0):
    avg = total / counter

    print(f"counter is {counter}")
    print(f"the average is {avg:.2f}")
    print(f"the total is {total}")

else:
    print("Error")
