import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Soccer Picks')
root.geometry('500x500')

group = ttk.Frame(root, padding=(20,20,20,20))
group.grid()

t = tk.StringVar()
t.set(0)


set_one = tk.Radiobutton(group, text="Team A", padx=20, variable=t, value=1, indicatoron=0)
set_one.pack()

set_two = tk.Radiobutton(group, text="Team B", padx=20, variable=t, value=2,indicatoron=0)
set_two.pack()


root.mainloop()
