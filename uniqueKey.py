print("Remove the duplicate data from a dictionary : ")
studentdata = {"id1":{"Name":"Alex","Class":"5th","Subject":"Coding"},
               "id2":{"Name":"Ambrika","Class":"5th","Subject":"Coding"},
               "id3":{"Name":"Sarah","Class":"5th","Subject":"Coding"},
               "id4":{"Name":"Alex","Class":"5th","Subject":"Coding"}}
result={}
seenkeys=[]
for studentid, details in studentdata.items():
    uniquekey=(details["Name"],details["Class"],details["Subject"])
    if uniquekey not in seenkeys:
        seenkeys.append(uniquekey)
        result[studentid]=details
for k,v in result.items():
    print(k,":",v)