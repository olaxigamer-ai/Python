try:
    age=int(input("Enter your age: "))
    if age%2==1:
        print("Your age is an odd number.")
    else:
        print("Your age is an even number")
except:
    print("Age is not valid. You must enter a number.")