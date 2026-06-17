from abc import ABC, abstractmethod
class absctclass(ABC):
    def print(self,x):
        print("X=",x)

    @abstractmethod
    def task(self):
        print("We are inside an abstract task")

class test_class(absctclass):
    def task(self):
        print("We are inside the test class task")

obj1= test_class()

obj1.task()

obj1.print(100)