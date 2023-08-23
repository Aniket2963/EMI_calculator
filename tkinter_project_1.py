from tkinter import*
from tkinter.messagebox import*
frame=Tk()
frame.title("EMI Calculator")
def calc():
    pr=int(p.get())
    rta=eval(r.get())
    tm=int(t.get())
    #calculation
    rt=rta/12/100
    em=(pr*rt*(1+rt)**tm)/((1+rt)**tm-1)
    emi.config(text=str(round(em)))
frame.geometry("600x500+500+40")
frame.resizable(False,False)
lbl=Label(frame,text="EMI Calculator",fg="Blue",font=("Arial 20 bold"))
lbl.place(x=200,y=20)
lb1=Label(frame,text="Loan amount in Rs :",font=("Arial 15 bold"))
lb1.place(x=50,y=100)
p=Entry(frame,font=("Arial 15"))
p.place(x=300,y=100)
#
lb2=Label(frame,text="Interest Rate in % p.a :",font=("Arial 15 bold"))
lb2.place(x=50,y=150)
r=Entry(frame,font=("Arial 15"))
r.place(x=300,y=150)
#
lb3=Label(frame,text="Period (in months) :",font=("Arial 15 bold"))
lb3.place(x=50,y=200)
t=Entry(frame,font=("Arial 15"))
t.place(x=300,y=200)
#creating calculate button
btn=Button(frame,text="Calculate",bg="Red",fg="white",font=("Arial 15 bold"),command=calc)
btn.place(x=250,y=250)
#
lb4=Label(frame,text="EMI : ",font=("Arial 20 bold"))
lb4.place(x=170,y=330)
emi=Label(frame,font=("Arial 30"))
emi.place(x=270,y=320)
frame.mainloop()















