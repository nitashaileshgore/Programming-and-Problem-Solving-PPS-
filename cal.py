from tkinter import *

window = Tk()

def Open():
    root = Tk()
    root.title("Waist to hip ratio")
    root.geometry("580x380+0+0")


    frame1 = Frame(root, pady=10, bd=16)
    frame1.grid()


    waist = StringVar()
    hip = StringVar()
    result = StringVar()
    conclusion = StringVar()

    frame2 = Frame(frame1, width=1000, height=300, pady=10, bd=16, relief="sunken")
    frame2.grid(row=0, column=0)

    frame3 = Frame(frame1, width=550, height=190, pady=10, bd=16, relief="sunken")
    frame3.grid(row=1, column=0)

    lblwaist = Label(frame2, text='Enter your waist circumference', font=('arial', 14, 'bold'), bd=12)
    lblwaist.grid(row=0, column=0, sticky=W)
    t1 = Entry(frame2, textvariable=waist, font=('arial', 14, 'bold'), bd=12)
    t1.grid(row=0, column=1, sticky=W)
    lblcm = Label(frame2, text='cm', font=('arial', 14, 'bold'), bd=12)
    lblcm.grid(row=0, column=2, sticky=W)

    lblhip = Label(frame2, text='Enter your hip circumference', font=('arial', 14, 'bold'), bd=12)
    lblhip.grid(row=1, column=0, sticky=W)
    t2 = Entry(frame2, textvariable=hip, font=('arial', 14, 'bold'), bd=12)
    t2.grid(row=1, column=1, sticky=W)
    lblcm = Label(frame2, text='cm', font=('arial', 14, 'bold'), bd=12)
    lblcm.grid(row=1, column=2, sticky=W)

    lblresult = Label(frame2, text='Show result', font=('arial', 14, 'bold'), bd=12)
    lblresult.grid(row=2, column=0, sticky=W)
    t3 = Entry(frame2, textvariable=result, font=('arial', 14, 'bold'), bd=12)
    t3.grid(row=2, column=1, sticky=W)

    lblconclusion = Label(frame2, text='conclusion', font=('arial', 14, 'bold'), bd=12)
    lblconclusion.grid(row=3, column=0, sticky=W)
    t4 = Entry(frame2, textvariable=conclusion, font=('arial', 14, 'bold'), bd=12)
    t4.grid(row=3, column=1, sticky=W)


    def add():
        f = float(t1.get())
        s = float(t2.get())
        a = f / s
        b = round(a, 2)
        t3.insert(END,str(b))
        if b < 0.95 or b == 0.95:
            t4.insert(END,"you have low health risk")
        elif b > 0.95 and b < 1.0:
            t4.insert(END,"you have moderate health risk")
        else:
            t4.insert(END,"you have higher health risk")

    def Reset():
        t1.delete(0,END)
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)

    def Exit():
        root.destroy()

    btnTotal = Button(frame3, text='Total', font=('arial', 14, 'bold'), bd=12, pady=12,width=8, command=add)
    btnTotal.grid(row=0, column=0)
    btnReset = Button(frame3, text='Reset', font=('arial', 14, 'bold'), bd=12, pady=12, width=8, command=Reset)
    btnReset.grid(row=0, column=1)
    btnExit = Button(frame3, text='Exit', font=('arial', 14, 'bold'), bd=12, pady=12, width=8, command=Exit)
    btnExit.grid(row=0, column=2)

    root.mainloop()


btn = Button(window,text="click hear to start", command=Open)
btn.place(x=80, y=150)
lbl = Label(window, text="MESCOE PUNE", font=("Helvetica", 16))
lbl.place(x=60, y=50)
lbl = Label(window, text="BMI CALCULATOR", font=("Helvetica", 16))
lbl.place(x=60, y=85)
lbl = Label(window, text="PBL GRP 3", font=("Helvetica", 16))
lbl.place(x=60, y=120)

window.title("STAY FIT STAY HEALTHY")
window.geometry("300x200+10+10")


window.mainloop()