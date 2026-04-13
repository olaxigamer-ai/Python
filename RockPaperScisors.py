import random
while True:
    user=input("Enter a choice (Rock, Paper, or Scisor) ")
    possible_actions=["Rock", "Paper", "Scisor"]
    computer=random.choice(possible_actions)
    print(f"\nYour Action {user}.\n")
    print("\n")
    print(f"\n computer action is {computer}.\n")
    if user==computer:
        print("Its a Tie")
    elif user=="Rock":
        if computer=="Scisor":
            print("You win!")
        else:
            print("You lose")
    elif user=="Scisor":
        if computer=="Paper":
            print("You win!")
        else:
            print("You lose")
    elif user=="Paper":
        if computer=="Rock":
            print("You win!")
        else:
            print("You lose")
    Play_Again=input("Do you want to play again (y/n): ")
    if Play_Again != "y":
        break