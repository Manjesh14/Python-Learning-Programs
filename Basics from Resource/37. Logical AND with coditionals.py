# Logical AND with if
age=20
nationality="Indian"

if (age>18 and age<30 and nationality=="Indian"):
    print("You are eligible for Exam")

# Logical And with if-else
age=32
nationality="Indian"

if (age>18 and age<30 and nationality=="Indian"):
    print("You are eligible for Exam")
else: print("you are not eligible for Exam")

# Logical AND with if-elif-else
age=20
nationality="American"

if (age>18 and age<30 and nationality=="Indian"):
    print("You are eligible for Exam : Fee=Rs 1500")
elif (age>18 and age<30 and nationality=="American"):
    print("You are eligible for Exam : Fee= $50")
else: print("you are not eligible for Exam")