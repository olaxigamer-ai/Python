print("Create a program to allow the student to do any exam if the student has a medical cause or more than 75% attendance")
medcause=input("Did you have a medical cause Y,N")
if medcause=='y':
    print("You are allowed to sit this exam")
else:
    attendance=int(input("Enter your attendance:"))
    if attendance>75:
        print("you are allowed to sit this exam")
    else:
        print("you are not allowed")