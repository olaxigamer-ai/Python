import array as arr
array_num=arr.array("i",[1,3,5,3,7,9,3])
print("The origional array : "+str(array_num))

#count number of occurence of the number 3
print("The number of occurance of the number 3 : "+str(array_num.count(3)))

#Reverse the Array
array_num.reverse()
print("Reversed order of items : ",array_num)