import tkinter
from PIL import ImageTk, Image
from tkinter import messagebox

def save_Note():
    title = title_entry.get()
    message = note_text.get('1.0', tkinter.END)
    key = key_entry.get()
    if title_entry.get() == "" or message == "" or key_entry.get() == "":
        messagebox.showinfo(title="Uyarı", message="Lütfen bütün bilgileri girin.")
    else:
        try:
            with open("secretNote.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{message}")
        except FileNotFoundError:
            with open("secretNote.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{message}")
        finally:
            title_entry.delete(0, tkinter.END)
            note_text.delete('1.0', tkinter.END)
            key_entry.delete(0, tkinter.END)

# Notepad
Notepad = tkinter.Tk()
Notepad.title("Secret NotePad")
Notepad.minsize(width=300, height=650)

# image
secret_img = ImageTk.PhotoImage(Image.open("top-secret.png").resize(size=[80, 80]))
imglabel = tkinter.Label(Notepad, image=secret_img)
imglabel.pack()

title_label = tkinter.Label(text="Enter your title")
title_label.pack()

title_entry = tkinter.Entry(width=20)
title_entry.pack()

note_label = tkinter.Label(text="Enter your Note")
note_label.pack()

note_text = tkinter.Text(width=30)
note_text.pack()

key_label = tkinter.Label(text="Enter Master key")
key_label.pack()

key_entry = tkinter.Entry(width=20)
key_entry.pack()

encrypt_button = tkinter.Button(text="Save and Encrypt", width=15, command=save_Note)
encrypt_button.pack()

decrypt_button = tkinter.Button(text="Decrypt", width=10)
decrypt_button.pack()

tkinter.mainloop()
