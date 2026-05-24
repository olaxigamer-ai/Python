class student:
    grade=8
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print("Name =",self.name)
        print("Age =",self.age)
        print("Grade =",self.grade)

student1=student("Alex",13)
Student2=student("Michael",12)

print(student1.display())
print(Student2.display())
