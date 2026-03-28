#24331A05G8
import tkinter as tk
def show():
    label.config(text=entry.get())
root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Submit", command=show)
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()