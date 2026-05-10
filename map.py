num1 = [1,2,3]
num2 = [4,5,6]
print("Origional list 1:",num1)
print("Origional list 2:",num2)
result = map(lambda x,y:x+y,num1,num2)
print("Addition of two lists:",list(result))

num3=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,num3))
print("Square of numbers in the list :",(square))