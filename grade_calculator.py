def calculator():
    name = input("Enter your name: ")
    subjects1 = int(input("Subject 1 marks: "))
    subjects2 = int(input("Subject 2 marks: "))
    subjects3 = int(input("Subject 3 marks: "))
    average = (subjects1 + subjects2 + subjects3) / 3
    
    if average <= 50:
        print("The student failed")
    else:
        print("The student passed")
    
calculator()