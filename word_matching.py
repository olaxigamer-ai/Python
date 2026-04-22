def matchword(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr=ctr+1
            lst.append(word)
    print("list of word with the same first and last charachters : \n", lst)
    return ctr
count=matchword(['123','abc','xyz','1221','aba'])
print("Number of words with the same first and last charachters", count)