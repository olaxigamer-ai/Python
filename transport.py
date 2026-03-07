print("select your mode of transport:")
print("1 for bike and 2 for car: ")
choice=int(input("enter your choice: "))
if choice==1:
    print("what type of bike?")
    print("1 for skooter and 2 for city bike")
    choice2=int(input("enter your second choice"))
    if choice2==1:
        print("you have selected scooter")
    else:
        print("you have selected city bike")
elif choice==2:
    print("1 for mazda and 2 for honda")
    choice3=int(input("enter your choice"))
    if choice3==1:
        print("you have selected mazda")
    else:
        print("you have selected honda")