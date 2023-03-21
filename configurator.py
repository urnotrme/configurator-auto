from tkinter import *

win = Tk()
win.title("Конфигуратор авто")
win.iconbitmap("icon.red.ico")
# размер и расположение окна
width_win = 700
height_win = 420

width_screen = win.winfo_screenwidth()
height_screen = win.winfo_screenheight()

middle_width = width_screen // 2
middle_height = height_screen // 2

win.geometry("{}x{}+{}+{}".format(width_win, height_win, middle_width - width_win // 2,
                                  middle_height - height_win // 2))
win.resizable(width=False, height=False)

# начальные данные
base_p = 1000000
pint = 0
pext = 0
pc = 0
ptrans = 0
price = base_p + pint + pext + pc + ptrans

# цена
label1 = Label(text=str(price)+" рублей", bg="plum", font=("Calibria", 20, "bold"))
label1.pack(fill=X)

# картинка
im = PhotoImage(file="gray.gif")
label2 = Label(image=im)
label2.pack(pady=15)

# цвета машин
frame1 = Frame(bg="lightgray", height=30)
frame1.pack(fill=X)
color = StringVar()
color.set("gray")


# функции
def f1():
    global pc
    global im
    if color.get() == "gray":
        pc = 0
        im = PhotoImage(file="gray.gif")
    elif color.get() == "blue":
        pc = 20000
        im = PhotoImage(file="blue.gif")
    elif color.get() == "red":
        pc = 100000
        im = PhotoImage(file="red.gif")
    elif color.get() == "green":
        pc = 20000
        im = PhotoImage(file="green.gif")
    elif color.get() == "purple":
        pc = 100000
        im = PhotoImage(file="violet.gif")
    elif color.get() == "chocolate":
        pc = 70000
        im = PhotoImage(file="chocolate.gif")

    label2.config(image=im)


def interior():
    global pint
    if op1.get() == 1:
        p_op1 = 90000
    else:
        p_op1 = 0

    if op2.get() == 1:
        p_op2 = 80000
    else:
        p_op2 = 0

    if op3.get() == 1:
        p_op3 = 50000
    else:
        p_op3 = 0
    pint = p_op1 + p_op2 + p_op3


def exterior():
    global pext
    if op4.get() == 1:
        p_op4 = 10000
    else:
        p_op4 = 0

    if op5.get() == 1:
        p_op5 = 4000
    else:
        p_op5 = 0

    if op6.get() == 1:
        p_op6 = 40000
    else:
        p_op6 = 0

    pext = p_op4 + p_op5 + p_op6


def transm():
    global ptrans

    if trans.get() == "auto":
        ptrans = 100000
    else:
        ptrans = 0


def calc():
    global price, base_p, pc, pint, pext, ptrans
    price = base_p + pint + pext + pc + ptrans
    label1.config(text=str(price)+" рублей")


# кнопки выбора цвета
color1 = Radiobutton(frame1, text="серый", fg="black", bg="darkgray", font=("Calibria", 10, "bold"),
                     activeforeground="darkgray", selectcolor="white", width=10, variable=color, value="gray",
                     command=f1)
color1.pack(side=LEFT, expand=1)
color2 = Radiobutton(frame1, text="голубой", fg="black", bg="skyblue", font=("Calibria", 10, "bold"),
                     activeforeground="skyblue", selectcolor="white", width=10, variable=color, value="blue",
                     command=f1)
color2.pack(side=LEFT, expand=1)
color3 = Radiobutton(frame1, text="зелёный", fg="black", bg="yellowgreen", font=("Calibria", 10, "bold"),
                     activeforeground="yellowgreen", selectcolor="white", width=11, variable=color, value="green",
                     command=f1)
color3.pack(side=LEFT, expand=1)
color4 = Radiobutton(frame1, text="шоколадный", fg="black", bg="sandybrown", font=("Calibria", 10, "bold"),
                     activeforeground="sandybrown", selectcolor="white", width=12, variable=color, value="chocolate",
                     command=f1)
color4.pack(side=LEFT, expand=1)
color5 = Radiobutton(frame1, text="сиреневый", fg="black", bg="orchid", font=("Calibria", 10, "bold"),
                     activeforeground="orchid", selectcolor="white", width=12, variable=color, value="purple",
                     command=f1)
color5.pack(side=LEFT, expand=1)
color6 = Radiobutton(frame1, text="красный", fg="black", bg="crimson", font=("Calibria", 10, "bold"),
                     activeforeground="crimson", selectcolor="white", width=11, variable=color, value="red",
                     command=f1)
color6.pack(side=LEFT, expand=1)


# интерьер
frame2 = Frame(win, bg="aliceblue")
frame2.pack(fill=X)

frame2_1 = LabelFrame(frame2, text="Интерьер", bg="lightpink")
frame2_1.pack(side=LEFT, expand=1, pady=10)
op1 = IntVar()
check1 = Checkbutton(frame2_1, text="Подогрев сидений", font=("Calibria", 10, "bold"), bg="lightpink", variable=op1,
                     onvalue=1, offvalue=0, command=interior)
op1.set(0)
check1.pack(anchor=W)

op2 = IntVar()
check2 = Checkbutton(frame2_1, text="Климат-контроль", font=("Calibria", 10, "bold"), bg="lightpink", variable=op2,
                     onvalue=1, offvalue=0, command=interior)
op2.set(0)
check2.pack(anchor=W)

op3 = IntVar()
check3 = Checkbutton(frame2_1, text="Центральный подлокотник", font=("Calibria", 10, "bold"), bg="lightpink",
                     variable=op3, onvalue=1, offvalue=0, command=interior)
op3.set(0)
check3.pack()

# экстерьер
frame2_2 = LabelFrame(frame2, text="Экстерьер", bg="lightpink")
frame2_2.pack(side=LEFT, expand=1, pady=10)

op4 = IntVar()
check4 = Checkbutton(frame2_2, text="Складывание боковых стёкол", font=("Calibria", 10, "bold"), bg="lightpink",
                     variable=op4, onvalue=1, offvalue=0, command=exterior)
op4.set(0)
check4.pack(anchor=W)

op5 = IntVar()
check5 = Checkbutton(frame2_2, text="Подкрылки", font=("Calibria", 10, "bold"), bg="lightpink", variable=op5,
                     onvalue=1, offvalue=0, command=exterior)
op5.set(0)
check5.pack(anchor=W)

op6 = IntVar()
check6 = Checkbutton(frame2_2, text="Видео-опция", font=("Calibria", 10, "bold"), bg="lightpink", variable=op6,
                     onvalue=1, offvalue=0, command=exterior)
op6.set(0)
check6.pack(anchor=W)

# Коробка передач
frame2_3 = LabelFrame(frame2, text="Коробка передач", bg="lightpink")
frame2_3.pack(side=LEFT, expand=1, pady=10)

trans = StringVar()
trans.set("mech")
trans1 = Radiobutton(frame2_3, text="Механическая", font=("Calibria", 10, "bold"), bg="lightpink", variable=trans,
                     value="mech", command=transm)
trans1.pack(anchor=W)

trans2 = Radiobutton(frame2_3, text="Автоматическая", font=("Calibria", 10, "bold"), bg="lightpink", variable=trans,
                     value="auto", command=transm)
trans2.pack()

# Кнопка "Расчитать"
frame3 = Frame(win)
frame3.pack(fill=X, side=BOTTOM)

btn = Button(frame3, text="Расчитать", font=("Calibria", 15, "bold"), fg="white", activeforeground="rosybrown",
             bg="rosybrown", relief=GROOVE, command=calc)
btn.pack(pady=15)

win.mainloop()
