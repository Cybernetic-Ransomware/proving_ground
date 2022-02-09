import tkinter as tk


WIN_SIZE = (800, 600)

root = tk.Tk()

root.geometry(f"{WIN_SIZE[0]}x{WIN_SIZE[1]}")
root.iconphoto(False, tk.PhotoImage(file='monkey.png'))
root.title('\U0001F4A3 This is sample bumple app!')


root.mainloop()
