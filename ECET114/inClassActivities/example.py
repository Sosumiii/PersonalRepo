#Elvis Nguyen
score = int(input("Enter your score"))

if (score >= 60):
    passedExam = True
else:
    passedExam = False

if passedExam:
    print("Good job! \nYou passed the exam!")
else:
    print("Take the exam again.")
""" score = int(input("What is your score? "))
if ((score > 100) or (score < 0)):
    print("This is an invalid value")

else:
    if (score >= 90):
        grade = "A"

    elif (score >= 80):
        grade = "B"

    elif (score >= 70):
        grade = "C"

    elif (score >= 60):
        grade = "D"

    else:
        grade = "F"

    print(f"Your grade is {grade}") """