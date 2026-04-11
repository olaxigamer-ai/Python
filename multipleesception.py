try:
    num1,num2=float(input("Enter two numbers separated by a comma , :"))
    result=num1/num2
    print("Your result is", result)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except SyntaxError:
    print("The comma is missing between your numbers.")
except:
    print("Wrong Input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what input")