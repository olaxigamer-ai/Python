def add(a,b):
    return a+b

def sub(a,b):
    return a-b


def divi(a,b):
    return a/b


def mult(a,b):
    return a*b

print("Please select the option: ")
print("a. addition b. subtraction c. division d. multiplication:")

choice=input("Enter your choice (a,b,c or d) : ")
num1=int(input("Please enter your first number : "))
num2=int(input("Enter your second number : "))

if choice=="a":
    print(add(num1,num2))
elif choice=="b":
    print(sub(num1,num2))
elif choice=="c":
    print(divi(num1,num2))
elif choice=="d":
    print(mult(num1,num2))
else:
    print("Invalid Input:")