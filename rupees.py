print("Finding any amount in 100s 50s and 10 rupees")
amount=int(input("enter any amount."))
n1=amount//100
n2=(amount%100)//50
n3=((amount%100)%50)//10

print("100 rupees note=",n1)
print("50 rupees note=",n2)
print("10 rupees note=",n3)