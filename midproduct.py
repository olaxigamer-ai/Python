num=int(input("enter a number more than 4 digits long: "))
t=num
numlength=0
while t>0:
    numlength=numlength+1
    t=int(t/10)
if numlength>=4:
    numlength=int(numlength/2)
    chk=0
    while num>0:
        rem=num%10
        if chk==numlength:
            midone=rem
        elif chk==numlength-1:
            midtwo=rem
        num=int(num/10)
        chk=chk+1
    product=midone*midtwo
    print("Product of mid digits is", product)
else:
    print("it is not a 4 or more digit number.")