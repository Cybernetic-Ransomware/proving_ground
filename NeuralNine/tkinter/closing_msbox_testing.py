import tkinter as tk
from tkinter import messagebox


WIN_SIZE = (800, 600)
BASIC_PADDING = min(WIN_SIZE) // 30
BASIC_FONT_TYPE = 'Verdana'


def on_closing():
    if messagebox.askyesno(title='Quit?', message='Are you sure?'):
        print('Destroying the World...')
        root.destroy()


root = tk.Tk()

root.geometry(f"{WIN_SIZE[0]}x{WIN_SIZE[1]}")
root.iconphoto(False, tk.PhotoImage(file='monkey.png'))
root.title('\U0001F4A3 This is sample bumple app!')
root.protocol('WM_DELETE_WINDOW', on_closing)


label = tk.Label(root, text='Monke!', font=(BASIC_FONT_TYPE, 24))
label.pack(padx=BASIC_PADDING, pady=BASIC_PADDING * 2)

textbox = tk.Text(root, height=5, width=WIN_SIZE[1], font=(BASIC_FONT_TYPE, 12))
textbox.pack(padx=BASIC_PADDING, pady=BASIC_PADDING)

pass_entry = tk.Entry(root, font=(BASIC_FONT_TYPE, 12), width=WIN_SIZE[1], show="*", justify='center')
pass_entry.pack(padx=BASIC_PADDING, pady=0)


btn_frame = tk.Frame(root)
btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)
btn_frame.columnconfigure(2, weight=1)
btn_frame.columnconfigure(3, weight=1)

btn_01 = tk.Button(btn_frame, text='Pull the monke!', font=(BASIC_FONT_TYPE, 10))
btn_01.grid(row=0, column=3, sticky=tk.E)


btn_frame.pack(padx=BASIC_PADDING, pady=BASIC_PADDING // 2, fill='x')

btn_02 = tk.Button(root, text='Don\'t rush the monke!', font=(BASIC_FONT_TYPE, 10), bg='grey', fg='white')
btn_02.place(x=WIN_SIZE[0] - 190, y=WIN_SIZE[1] - 270, height=30, width=170)


root.mainloop()
