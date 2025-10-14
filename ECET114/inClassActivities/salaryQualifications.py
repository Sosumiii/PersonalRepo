salary = int(input("Enter your salary: "))
yearsOnJob = int(input("Enter the amount of years you spent on the job: "))


"""
if ((salary >= 30000) and (yearsOnJob > 5)):
    print("This person is qualified.")
else:
    print("This person is not qualified.")
"""

con1 = salary >= 30000 and yearsOnJob >= 2
con2 = salary < 30000 and yearsOnJob >= 5

if (con1) or (con2):
    print("qualified")

else:
    print("Not qualified")