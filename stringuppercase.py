class iostring():
    def __init__ (self):
        self.string1=""

    def getstring(self):
        self.string1=input("Enter any string : ")

    def print_string(self):
        print("Result is : ", self.string1.upper())

string1=iostring()
string1.getstring()
string1.print_string()