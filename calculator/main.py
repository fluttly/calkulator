import tkinter as tk
from tkinter import *
from tkinter import messagebox


def calculate_shashlik():
    m90: int = int(male_90_ent.get())
    m: int = int(male_ent.get())
    f70: int = int(fem_70_ent.get())
    f: int = int(fem_ent.get())
    ch: int = int(child_ent.get())
    shashlik = (m90 * 0.6) + (m * 0.5) + (f70 * 0.5) + (f * 0.4) + (ch * 0.3)
    shashlik = round(shashlik, 1)
    if m90 < 0:
        messagebox.showinfo('shahlik', f'Ты че воодишь, уважаемый, как у тебя люди в минус ушли??')
    elif m < 0:
        messagebox.showinfo('shahlik', f'Ты че воодишь, уважаемый, как у тебя люди в минус ушли??')
    elif f70 < 0:
        messagebox.showinfo('shahlik', f'Ты че воодишь, уважаемый, как у тебя люди в минус ушли??')
    elif f < 0:
        messagebox.showinfo('shahlik', f'Ты че воодишь, уважаемый, как у тебя люди в минус ушли??')
    elif ch < 0:
        messagebox.showinfo('shahlik', f'Ты че воодишь, уважаемый, как у тебя люди в минус ушли??')
    else:
        messagebox.showinfo('shashlik', f'{shashlik} килограмм шашлыка закупать надо')

root = Tk()
root.title("Калькулятор шашлыка")
root.geometry('600x600')

frame = Frame(
    root,
    padx=10,
    pady=10
)
frame.pack(expand=True)

male_90 = Label(
    frame,
    text="Мужчин, весом более 90кг"
)
male_90.grid(row=3, column=2)
male = Label(
    frame,
    text="Мужчин весом менee 90кг"
)
male.grid(row=4, column=2)
fem_70 = Label(
    frame,
    text="Женщин весом более 70кг"
)
fem_70.grid(row=5, column=2)
fem = Label(
    frame,
    text="Женщин весом менее 70кг"
)
fem.grid(row=6, column=2)
child = Label(
    frame,
    text="Детей"
)
child.grid(row=7, column=2)

male_90_ent = Entry(
    frame,

)
male_90_ent.insert(0, "0")
male_90_ent.grid(row=3, column=1, pady=10)
male_ent = Entry(
    frame,

)
male_ent.insert(0, "0")
male_ent.grid(row=4, column=1, pady=10)
fem_70_ent = Entry(
    frame,
)
fem_70_ent.insert(0, "0")
fem_70_ent.grid(row=5, column=1, pady=10)
fem_ent = Entry(
    frame,

)
fem_ent.insert(0, "0")
fem_ent.grid(row=6, column=1, pady=10)
child_ent = Entry(
    frame,
)
child_ent.insert(0, "0")
child_ent.grid(row=7, column=1, pady=10)

cal_btn = Button(
    frame,
    text='Рассчитать',
    command=calculate_shashlik
)
cal_btn.grid(row=8, column=1, pady=10)

root.mainloop()
