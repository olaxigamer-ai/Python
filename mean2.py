print("Mean of 40 numbers is 38 but, 56 is misread as 36. Find the correct mean.")

mean1=38
wrong_num=36
correct_num=56
total_num=40

sum=mean1*total_num
print("the sum of 40 numbers is",sum)

num2=sum-(wrong_num-correct_num)
print("difference=",num2)
mean=num2/total_num
print("The correct mean is:",mean)
