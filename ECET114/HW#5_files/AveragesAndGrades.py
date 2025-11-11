#Elvis Nguyen
#Test averages and grades

def calc_average(value1: float, value2: float, value3: float, value4: float, value5: float):
    """ Takes 5 values and calculates the average """
    sum = value1 + value2 + value3 + value4 + value5
    return sum / 5

def determine_grade(grade: float):
    """ Determines the letter grade for a singular test """
    if (grade <= 100 and grade >= 90):
        return "A"
    elif (grade <= 89 and grade >= 80):
        return "B"
    elif (grade <= 79 and grade >= 70):
        return "C"
    elif (grade <= 69 and grade >= 60):
        return "D"
    else:
        return "F"


def main():
    grades = []#Used a list here for more efficiency

    for grade in range(5): 
        points = float(input("Enter your grade value: "))
        grades.append(points)

    avg = calc_average(grades[0], grades[1], grades[2], grades[3], grades[4])
    print(f"The average score out of 5 tests are {avg:.1f} and the letter grade is {determine_grade(avg)}")

    for grade in range(len(grades)):
        print(f"The score for test {grade + 1} is {grades[grade]}. The letter grade for that test is {determine_grade(grades[grade])}")

main()