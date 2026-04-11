try:
    num=int(input("Enter a number : "))
    print("Your number is", num)
except ValueError as ex:
    print("Exception", ex)
print("I love coding")