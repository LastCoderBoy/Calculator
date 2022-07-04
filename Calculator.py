from tkinter import *
import math

print('Calculator is working now...')

window = Tk()
window.title('Simple Calculator')
window.geometry('451x458')
#window.iconbitmap('C:/Users/12345/Desktop/calculator.ico')
window.config(bg='#4e5e5e')
window.resizable(width=False, height=False)

frame= Frame(window,bg='#4e5e5e')
frame.pack()


entry = Entry(frame,bd=4, justify="right", font=('Fonte', 20, 'bold'))

entry.grid(row=0,column=0, columnspan=5, ipadx=25, ipady=20, padx=10, pady=10, )


def press(number):
    now = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(now) + str(number))


def button_clear():
    entry.delete(0,END)


def button_add():
    first = entry.get()
    global f_num
    f_num = float(first)
    global math
    math = 'addition'
    entry.delete(0, END)


def button_sub():
    first = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = float(first)
    entry.delete(0, END)


def button_multi():
    first = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first)
    entry.delete(0, END)


def button_divide():
    first = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first)
    entry.delete(0, END)


def square_root():
    now = entry.get()
    entry.delete(0, END)
    Root = math.sqrt(float(now))
    entry.insert(0, Root)

def cos():
    now = entry.get()
    entry.delete(0, END)
    Cosinus = math.cos(math.radians(float(now)))
    entry.insert(0, Cosinus)


def sin():
    now = entry.get()
    entry.delete(0, END)
    Sinus = math.sin(math.radians(float(now)))
    entry.insert(0, Sinus)



def square_power():
    now = entry.get()
    entry.delete(0, END)
    Percent = int(now)**2
    entry.insert(0, Percent)


def tg():
    now = entry.get()
    entry.delete(0, END)
    Tanginus = math.tan(math.radians(float(now)))
    entry.insert(0, Tanginus)


def percentage():
    now = entry.get()
    entry.delete(0, END)
    Percent = float(now)/100
    entry.insert(0, Percent)

def negative_int():
    now = -(float(entry.get()))
    entry.delete(0, END)
    entry.insert(0, now)



def backspace():
    now = len(entry.get())
    entry.delete(now-1, END)


def button_equal():
    second = entry.get()
    entry.delete(0, END)
    if math == 'subtraction':
        entry.insert(0, f_num - float(second))
    elif math == 'addition':
        entry.insert(0, f_num + float(second))
    elif math == 'multiplication':
        entry.insert(0, f_num * float(second))
    elif math == 'division':
        entry.insert(0, f_num / float(second))


#Number buttons
button_1= Button(frame,text='1',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=lambda: press(1))

button_2= Button(frame,text='2',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=lambda: press(2))

button_3= Button(frame,text='3',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=lambda: press(3))

button_4= Button(frame,text='4',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=lambda: press(4))

button_5= Button(frame,text='5',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=lambda: press(5))

button_6= Button(frame,text='6',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=lambda: press(6))

button_7= Button(frame,text='7',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=lambda: press(7))

button_8= Button(frame,text='8',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=lambda: press(8))


button_9= Button(frame,text='9',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=lambda: press(9))

button_0= Button(frame,text='0',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=lambda: press(0))

button_dot1= Button(frame,text='.',font=('Fonte',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=lambda: press('.'))

PLus_Minus= Button(frame,text='±',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#707070", fg='white', width=8, height=3, command=negative_int)

#math button symbols

Subtraction= Button(frame,text='–',fg='#182324' ,font=('Times New Roman',13, 'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command=button_sub)

Clear_button= Button(frame,text='C',fg='red' ,font=('Fonte',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command=button_clear)

Equal= Button(frame,text='=',fg='#182324',font=('Fonte',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3,command=button_equal)

Addition= Button(frame,text='+',fg='#182324',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command=button_add)

Multiplication= Button(frame,text='x',fg='#182324' ,font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command=button_multi)

Division= Button(frame,text='/',fg='#182324' ,font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command=button_divide)

Power= Button(frame,text='x²',fg='#182324' ,font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command=square_power)

Percentage= Button(frame,text='%',fg='#182324' ,font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command=percentage)

Backspace= Button(frame,text='⌫',fg='#182324',font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command=backspace)

Sqr_root= Button(frame,text='√',fg='#182324' ,font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command=square_root)

Cosine= Button(frame,text='cos',fg='#182324' ,font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command=cos)

Sine= Button(frame,text='sin',fg='#182324' ,font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command= sin)

Tangent= Button(frame,text='tan',fg='#182324' ,font=('Times New Roman',13,'bold'), relief='ridge',
                 bd=2, bg="#b0b0b0", width=8, height=3, command= tg)

#Showing buttons
button_7.grid(row=2, column=1)
button_8.grid(row=2, column=2)
button_9.grid(row=2, column=3)

button_4.grid(row=3, column=1)
button_5.grid(row=3, column=2)
button_6.grid(row=3, column=3)

button_1.grid(row=4, column=1)
button_2.grid(row=4, column=2)
button_3.grid(row=4, column=3)

button_0.grid(row=5, column=2)
button_dot1.grid(row=5, column=3)

#showing math symbols

Division.grid(row=2, column=4)
Multiplication.grid(row=1, column=4)
Subtraction.grid(row=3, column=4)
Addition.grid(row=4, column=4)

Sqr_root.grid(row=1, column=3)
PLus_Minus.grid(row=5, column=1)
Power.grid(row=1, column=2)
Percentage.grid(row=5, column=0)

Clear_button.grid(row=1, column=0)
Backspace.grid(row=1, column=1)
Equal.grid(row=5, column=4)

Cosine.grid(row=3, column=0)
Sine.grid(row=2, column=0)
Tangent.grid(row=4, column=0)




window.mainloop()

print('Calculator stopped!')