# using tkinter for gui interface
from tkinter import *

window=Tk()
window.geometry("700x500")
# calculation code
def calculate():
    # default

    espresso=e1.get()
    if not espresso:
        espresso = 0
    cafe_latte=e2.get()
    if not cafe_latte:
        cafe_latte = 0
    cappuccino=e3.get()
    if not cappuccino:
        cappuccino = 0

    americano=e4.get()
    if not americano:
        americano = 0
    choclate_sandwich=e5.get()
    if not choclate_sandwich:
        choclate_sandwich = 0
    sandwich=e6.get()
    if not sandwich:
        sandwich = 0
    brownie=e7.get()
    if not brownie:
        brownie = 0
    total=(int(espresso)*150+int(cafe_latte)*170+int(cappuccino)*200+int(americano)*150+int(choclate_sandwich)*210+int(sandwich)*150+int(brownie)*110)
    label102=Label(window,text="TOTAL=",font="times 22 bold italic")
    label102.place(x=250,y=450)

    label101=Label(window,text=total,font="times 22  bold")
    label101.place(x=400,y=450)
# menu section
label101=Label(window,text="Cofee Shop",font="times 35 italic bold")
label101.place(x=350,y=20,anchor="center")

label1=Label(window,text="MENU",font="times 30 bold")
label1.place(x=450, y=70)

label2=Label(window,text="Cofee",font="times 25 italic bold")
label2.place(x=500, y=120)

label3=Label(window,text="Espresso             $150",font="times 20 italic")
label3.place(x=450, y=160)

label3=Label(window,text="Cafe latte           $170",font="times 20 italic")
label3.place(x=450, y=190)

label3=Label(window,text="Cappuccino       $200",font="times 20 italic")
label3.place(x=450, y=220)

label3=Label(window,text="Americano        $150",font="times 20 italic")
label3.place(x=450, y=250)

label4=Label(window,text="Desserts",font="times 25 italic bold")
label4.place(x=500,y=280)

label5=Label(window,text="Choclate Sandwich     $210",font="times 19")
label5.place(x=420,y=320)

label6=Label(window,text="Sandwich                     $150",font="times 19 ")
label6.place(x=420,y=350)

label7=Label(window,text="Brownie                       $110",font="times 19")
label7.place(x=420,y=380)

# billing part
label100=Label(window,text="   Item Section",font="times 23 bold italic")
label100.place(x=20,y=80)
label8=Label(window,text="Espresso",font="times 18")
label8.place(x=20,y=120)

e1=Entry(window)
e1.place(x=210,y=125)

label8=Label(window,text="Cafe Latte",font="times 18")
label8.place(x=20,y=150)
e2=Entry(window)
e2.place(x=210,y=155)

label8=Label(window,text="Cappaccino",font="times 18")
label8.place(x=20,y=180)
e3=Entry(window)
e3.place(x=210,y=185)

label8=Label(window,text="Americano",font="times 18")
label8.place(x=20,y=210)
e4=Entry(window)
e4.place(x=210,y=215)



label8=Label(window,text="Choclate Sandwich",font="times 18")
label8.place(x=20,y=250)
e5=Entry(window)
e5.place(x=210,y=255)

label8=Label(window,text="Sandwich",font="times 18")
label8.place(x=20,y=280)
e6=Entry(window)
e6.place(x=210,y=285)

label8=Label(window,text="Brownie",font="times 18")
label8.place(x=20,y=310)
e7=Entry(window)
e7.place(x=210,y=315)

b2=Button(window,text="bill",width=20,command=calculate)
b2.place(x=210,y=350)

window.mainloop()