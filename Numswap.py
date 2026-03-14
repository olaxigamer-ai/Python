print("you are doing a question that requires you to give the values for three variables. AxB+C")

a=int(input("enter A: "))
b=int(input("enter B: "))
c=int(input("enter C"))
print(a*b+c)

print("you can now switch the numbers where a will become in b spot b will be in c and c in a")

a=b
c=a
b=c

print(a*b+c)