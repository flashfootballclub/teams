import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title = "Champions League Matches"
root.geometry("200x500")

frame = ttk.Frame(root)
frame.grid(row=0)


one = tk.StringVar()
one.set(f" ")


match_one = [
    "Juventus",
    "DRAW",
    "Lyon"
]



def show_pick():
    print(one.get())




for val, team in enumerate(match_one):
    first_match = tk.Radiobutton(frame,
                                 text=team,
                                 variable=one,
                                 command=show_pick,
                                 value=team,
                                 indicatoron=0,
                                 bg="light blue",
                                 padx=10,

                                 )
    first_match.grid(columnspan=1, sticky="ew")


label_picks = tk.Label(frame, textvariable=one)
label_picks.grid(row=4)

root.mainloop()
