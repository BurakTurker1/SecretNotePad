import tkinter
from PIL import ImageTk, Image

# Notepad
Notepad = tkinter.Tk()
Notepad.title("Secret NotePad")
Notepad.minsize(width=300, height=650)

# image
secret_img = ImageTk.PhotoImage(Image.open("top-secret.png").resize(size=[80,80]))
imglabel = tkinter.Label(Notepad, image=secret_img).pack()

title_label=tkinter.Label(text="Enter your title",)
title_label.pack()

title_entry=tkinter.Entry(width=20)
title_entry.pack()

note_label=tkinter.Label(text="Enter your Note ")
note_label.pack()

note_text=tkinter.Text(width=30)
note_text.pack()

key_label=tkinter.Label(text="Enter Master key")
key_label.pack()

key_entry=tkinter.Entry(width=20)
key_entry.pack()

encrypt_button = tkinter.Button(text="Save and Encrypt", width=15)
encrypt_button.pack()

decrypt_button = tkinter.Button(text="Decrypt",width=10)
decrypt_button.pack()

tkinter.mainloop()
