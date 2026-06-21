class Book:
    is_borrowed=False
    def __init__(self,title,author,is_borrowed):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    def Borrow(self):
        self.is_borrowed=True
        print(self.title,"is borrowed.")

    def return_book(self):
        self.is_borrowed=False
        print(self.title,"Has been returned.")
    
HaryPotter=Book("Hary Potter","JK Rowling",False)
HaryPotter.Borrow()
HaryPotter.return_book()
ti=Book("Treasure Island", "RL stevenson",False)
ti.Borrow()
ti.return_book()
book3=Book("Book3","Alex",False)
book3.Borrow()
book3.return_book()