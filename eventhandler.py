from tkinter import *

window=Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    print(event.char)

window.bind("<KeyPress>",handle_keypress)

def handle_click(event):
    print("\nThe button was clicked!")

btn=Button(text="Click Me")

btn.pack()

btn.bind("<Button-1>",handle_click)

window.mainloop()