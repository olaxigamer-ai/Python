class person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print("Name=",self.name)
        print("Id=",self.idnumber)

class employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)
    def display2(self):
        print("Salary=",self.salary)
        print("Post=",self.post)
object1=employee("Alex",3213,100000,"Manager")

object1.display()
object1.display2()