class myclass:
    __privatevar=27
    def __privatemethod(self):
        print("I am inside class MY class")
    def hello(self):
        print("Private variable value:",myclass.__privatevar)

obj=myclass()
obj.hello()
obj.__privatemethod