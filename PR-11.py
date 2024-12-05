from tkinter import*
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter.ttk import Checkbutton
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu
import tkinter as tk
def clicked1():
    value1=float(txt1.get())
    value2=float(txt2.get())
    if combo.get()=='+':
        Result=value1+value2
    if combo.get()=='-':
        Result=value1-value2
    if combo.get()=='*':
        Result=value1*value2
    if combo.get()=='/':
        Result=value1/value2
    lbl1 = Label(tab1, text='Результат')
    lbl1.configure(text=f"Результат {Result}")
    lbl1.grid(column = 4, row = 4)
def clicked2():
    selected_options = []
    if var1.get():
        selected_options.append("первый вариант")
    if var2.get():
        selected_options.append("второй вариант")
    if var3.get():
        selected_options.append("третий вариант")
    if selected_options:
        messagebox.showinfo("Выбор", "Вы выбрали: " + " и ".join(selected_options))
    else:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")
def load_text():
    file_path = filedialog.askopenfilename(title="Выберите файл", filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")))
    with open(file_path, 'r', encoding='utf-8') as file:
        for text_content in file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, text_content)
window=Tk()
window.title('Семилуцкий Иван Андреевич')
window.geometry('600x400')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Работа с текстом')
tab_control.pack(expand=1, fill='both')
lbl1 = Label(tab1, text='Результат')
lbl1.grid(column =0 , row = 0)
btn = Button(tab1, text="Посчитать", command=clicked1)
btn.grid(column=4, row=1)
txt1 = Entry(tab1, width=10)
txt1.grid(column=0, row=1)
txt2 = Entry(tab1, width=10)
txt2.grid(column=3, row=1)
combo = Combobox(tab1)
combo['values'] = ('Что сделать?','+','-','*','/')
combo.current(0)
combo.grid(column=2, row=1)
var1=BooleanVar()
var2=BooleanVar()
var3=BooleanVar()
chk1 = Checkbutton(tab2, text='Выбрать', variable=var1)
chk1.grid(column=0, row=0)
chk2 = Checkbutton(tab2, text='Выбрать', variable=var2)
chk2.grid(column=1, row=0)
chk3 = Checkbutton(tab2, text='Выбрать', variable=var3)
chk3.grid(column=2, row=0)
btn = Button(tab2, text="Выбрать", command=clicked2)
btn.grid(column=4, row=0)
lbl2 = Label(tab2, text='Результат')
lbl2.grid(column =0 , row = 1)
menu = Menu(window)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Открыть', command=load_text)
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
text = Text(tab3, width=500, height=300, bg="white", fg='black', font='Arial', wrap=WORD)
text.pack(expand=1, fill='both')
window.mainloop()