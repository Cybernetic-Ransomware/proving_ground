import tkinter as tk
from tkinter import messagebox


WIN_SIZE = (800, 600)
BASIC_PADDING = min(WIN_SIZE) // 30
BASIC_FONT_TYPE = 'Verdana'


class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WIN_SIZE[0]}x{WIN_SIZE[1]}")
        self.root.iconphoto(False, tk.PhotoImage(file='monkey.png'))
        self.root.title('\U0001F4A3 This is sample bumple app!')

        self.lbl_001 = tk.Label(self.root, text='Input your message:', font=(BASIC_FONT_TYPE, 24))
        self.lbl_001.pack(padx=BASIC_PADDING, pady=BASIC_PADDING * 2)

        self.txb_001 = tk.Text(self.root, height=5, width=WIN_SIZE[1], font=(BASIC_FONT_TYPE, 12))
        self.txb_001.pack(padx=BASIC_PADDING, pady=BASIC_PADDING)

        self.chk_btn_001_state = tk.BooleanVar()
        self.chk_btn_001 = tk.Checkbutton(self.root, text='Pull that message?', font=(BASIC_FONT_TYPE, 12),
                                          variable=self.chk_btn_001_state)
        self.chk_btn_001.pack(padx=BASIC_PADDING, pady=BASIC_PADDING)

        self.btn_001 = tk.Button(self.root, text='Rush the monke!', font=(BASIC_FONT_TYPE, 10), bg='grey', fg='white',
                                 command=self.show_message)
        self.btn_001.pack(padx=BASIC_PADDING, pady=BASIC_PADDING)

        self.root.mainloop()

    def show_message(self):
        if self.chk_btn_001_state.get():
            print(self.txb_001.get('1.0', tk.END))
            messagebox.showinfo(title='Response',
                                message=f"Did you said \"{(self.txb_001.get('1.0', tk.END)).lower()[:-1]}\"?")
        else:
            print('Monke doesn\'t response')


MyGUI()
