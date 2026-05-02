mydict={"codingal":2,"is":2,"best":2,"for":2,"coding":1}
print("The origional dictionary : "+str(mydict))
value=2
counter=0
for key in mydict:
    if mydict[key]==value:
        counter=counter+1
        print("frequency of 2 is : "+str(counter))
