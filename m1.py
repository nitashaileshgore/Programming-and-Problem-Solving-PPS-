'''
def add(a,b):
    print("name of module:",__name__)
    c=a+b
    return c
'''
from tkinter import *
window=Tk()
btn=Button(window, text="Click me", fg='blue')
bt1=Button(window,text="submit",fg='red')
btn.place(x=80, y=100)
bt1.place(x=150,y=50)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()