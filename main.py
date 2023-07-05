import tkinter
from PIL import ImageTk, Image
from tkinter import messagebox
import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
def save_Note():
    title = title_entry.get()
    message = note_text.get('1.0', tkinter.END)
    key = key_entry.get()
    if title_entry.get() == "" or message == "" or key_entry.get() == "":
        messagebox.showinfo(title="Uyarı", message="Lütfen bütün bilgileri girin.")
    else:
        encrypt_message = encode(key, message)
        try:
            with open("secretNote.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{encrypt_message}")
        except FileNotFoundError:
            with open("secretNote.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{encrypt_message}")
        finally:
            title_entry.delete(0, tkinter.END)
            note_text.delete('1.0', tkinter.END)
            key_entry.delete(0, tkinter.END)
def decrypt_Note():
    key=key_entry.get()
    encrypt_note=note_text.get('1.0',tkinter.END)
    if encrypt_note == "" or key_entry.get() == "":
        messagebox.showinfo(title="Uyarı", message="Lütfen bütün bilgileri girin.")
    else:
        try:
            decrrypt_note=decode(key,encrypt_note)
            note_text.delete('1.0', tkinter.END)
            note_text.insert('1.0', decrrypt_note)
        except:
            messagebox.showerror("uyarı", message="lütfen şifreli bir mesaj giriniz")
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

decrypt_button = tkinter.Button(text="Decrypt", width=10,command=decrypt_Note)
decrypt_button.pack()

tkinter.mainloop()
