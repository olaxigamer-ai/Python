word=input("Enter your word")
char=input("enter your charachter: ")

i=0
count=0
while i<len(word):
    if word[i]==char:
        count=count+1
    i=i+1
print("the total number of times it occured was", count)