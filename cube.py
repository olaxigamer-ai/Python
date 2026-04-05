print("Find out the cube of the given number and check if the number is divisible by 3 : ")
def cube(num):
    return num*num*num
def div_by_three(num):
    if num%3==0:
        return cube(num)
    else:
        return False
print(div_by_three(9))
print(div_by_three(8))
