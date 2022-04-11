
from tkinter import *
from tkinter import ttk
win = Tk()
win.geometry("500x200+10+20")
win.title("Midterm in OOP")

btn = Button(win, text="Click to display your Fullname", fg="red", bg="white", font=("times new roman", 10))
btn.place(x=50, y=100)

lbl1 = Label(win, text="Enter your fullname: ", fg="red")
lbl1.place(x=50, y=50)

lbl2 = Label(win, fg="red")
lbl2.place(x=250, y=100)

txt = Entry(win, bd=5)
txt.place(x=250, y=50)

txt2 = Entry(win, font=("times new roman", 12), bd=5)
txt2.place(x=250, y=100)

win.mainloop()