# grade_calculator.py

name = input("Enter your name: ")
subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))

average = (subject1 + subject2 + subject3) / 3

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
elif average >= 50:
    grade = 'E'
else:
    grade = 'F'

if average >= 50:
    result = "Student passed"
else:
    result = "Student failed"


print(f"\nStudent Name: {name}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
print(f"Result: {result}")
