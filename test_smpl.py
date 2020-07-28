import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Soccer Picks')
root.geometry('500x500')

group = ttk.Frame(root, padding=(20,20,20,20),)
group.pack()

group_two = ttk.Frame(root)
group_two.grid(row=1)

t = tk.StringVar()
t.set(f" ")

t_two = tk.StringVar()
t.set(f" ")

teams = [
    "Barcelona",
    "Real Madrid",
    "City",
    "Outdoors"
]

teams_two = [
    "Dourtmund",
    "PSG",
    "Atlanta United",
    "LA Galaxy"
]


def show_result():
    print(t.get())


def show_result_two():
    print(t.get())


for val, team in enumerate(teams):
    tk.Radiobutton(group,
                   text=team,
                   padx=20,
                   variable=t,
                   command=show_result,
                   value=team,
                   indicatoron=0,
                   bg="light blue").pack(side="left")

for val, team_two in enumerate(teams_two):
    tk.Radiobutton(group_two,
                   text=team_two,
                   padx=20,
                   variable=t_two,
                   command=show_result_two,
                   value=team_two,
                   indicatoron=0,
                   bg="light green"
                   ).grid(sticky="ew")

result = ttk.Label(group, textvariable=t)
result.pack(side="bottom")

# result_two = ttk.Label(group_two, textvariable=t_two)
# result_two.grid()


root.mainloop()
