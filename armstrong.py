n=int(input("Enter any number: "))
sum=0
temp=n
while temp>0:
    dizit=temp%10
    sum=sum+dizit**3
    temp=temp//10
if n==sum:
    print("Number is an armstrong number")
else:
    print("number is not an armstrong number")