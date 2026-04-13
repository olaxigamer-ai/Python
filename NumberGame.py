import random
playing= True
num=str(random.randint(0,9))
print("I will genarate a number from 0-9 and you have to guess the number:")
while playing:
    guess=input("What is your guess? : ")
    if num==guess:
        print("You won!!!")
        print("The number was", num)
        break
    else:
        print("Try again")
        print("The number was", num)