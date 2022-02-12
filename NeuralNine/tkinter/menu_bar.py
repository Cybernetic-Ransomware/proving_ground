import tkinter as tk


WIN_SIZE = (800, 600)
BASIC_PADDING = min(WIN_SIZE) // 30
BASIC_FONT_TYPE = 'Verdana'


def show_message():
    print('Nothing much, BRB!')


def clear():
    textbox.delete('1.0', tk.END)
    pass_entry.delete(0, 'end')


root = tk.Tk()

root.geometry(f"{WIN_SIZE[0]}x{WIN_SIZE[1]}")
root.iconphoto(False, tk.PhotoImage(file='monkey.png'))
root.title('\U0001F4A3 This is sample bumple app!')


menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Close', command=exit)
file_menu.add_separator()
file_menu.add_command(label='Do this same as previous', command=exit)

action_menu = tk.Menu(menu_bar, tearoff=0)
action_menu.add_command(label='Show me more', command=show_message)

menu_bar.add_cascade(menu=file_menu, label='File')
menu_bar.add_cascade(menu=action_menu, label='Click now!')
root.config(menu=menu_bar)


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

btn_03 = tk.Button(root, text='Clear text fields', font=(BASIC_FONT_TYPE, 10), bg='white', fg='grey', command=clear)
btn_03.place(x=WIN_SIZE[0] - 190, y=WIN_SIZE[1] - 230, height=30, width=170)


root.mainloop()
