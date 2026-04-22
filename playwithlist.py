l=[5,3,6,4,2,8,3,1,99]
print("Original list is:", l)
count=0
for i in l:
    count=count+i
average=count/len(l)
print("Sum =", count)
print("Average =", average)
l.sort()
print(l)
print("Smallest element is", l[0])
print("Largest element is", l[-1])