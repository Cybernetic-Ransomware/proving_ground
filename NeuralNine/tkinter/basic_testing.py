import tkinter as tk


WIN_SIZE = (800, 600)
BASIC_PADDING = min(WIN_SIZE) // 30
BASIC_FONT_TYPE = 'Verdana'


root = tk.Tk()

root.geometry(f"{WIN_SIZE[0]}x{WIN_SIZE[1]}")
root.iconphoto(False, tk.PhotoImage(file='monkey.png'))
root.title('\U0001F4A3 This is sample bumple app!')


label = tk.Label(root, text='Monke!', font=(BASIC_FONT_TYPE, 24))
label.pack(padx=BASIC_PADDING, pady=BASIC_PADDING * 2)

textbox = tk.Text(root, height=5, width=WIN_SIZE[1], font=(BASIC_FONT_TYPE, 12))
textbox.pack(padx=BASIC_PADDING, pady=BASIC_PADDING)

pass_entry = tk.Entry(root, font=(BASIC_FONT_TYPE, 12), width=WIN_SIZE[1], show="*", justify='center')
pass_entry.pack(padx=BASIC_PADDING, pady=0)

button = tk.Button(root, text='Pull the monke!', font=(BASIC_FONT_TYPE, 10))
button.pack(padx=BASIC_PADDING, pady=BASIC_PADDING // 2)


root.mainloop()
