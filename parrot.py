class parrot:
    species='Bird'
    def __init__(self,name,age):
        self.name=name
        self.age=age

obj1=parrot('blu',15)
obj2=parrot('Woo',12)

print("Blu is a",obj1.species)
print("Woo is also a",obj2.species)
print(obj1.name,"Is", obj1.age,"Years old.")
print(obj2.name,"Is", obj2.age,"Years old.")