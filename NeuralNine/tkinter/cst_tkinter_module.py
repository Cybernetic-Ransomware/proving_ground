from doctest import master

import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry('600x800')
root.title('Testing color schemes')


flag_ch_01 = customtkinter.BooleanVar()


def login():
    if flag_ch_01.get():
        print('You will never loggout')
        root.destroy()
    else:
        print('Tests are halfway done')


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text='Login page', text_font=('Helvetica', 20))
label.pack(pady=24, padx=10)

entry_01 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry_01.pack(pady=12, padx=10)

entry_02 = customtkinter.CTkEntry(master=frame, placeholder_text="Password")
entry_02.pack(pady=12, padx=10)

button_01 = customtkinter.CTkButton(master=frame, text='Login', command=login)
button_01.pack(pady=12, padx=10)

checkbox_01 = customtkinter.CTkCheckBox(master=frame, text='Don\'t log out', variable=flag_ch_01)
checkbox_01.pack(pady=12, padx=10)

root.mainloop()
