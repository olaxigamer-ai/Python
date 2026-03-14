num=int(input("Enter your number: "))
count=0
while num!=0:
    num=num//10
    count=count+1
print(count)