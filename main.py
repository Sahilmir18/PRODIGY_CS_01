from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("400x400")

tk.Label(window, text = "Welcome to Caesar Cipher").pack(anchor='w')
tk.Label(window, text = " ").pack(anchor='w')
tk.Label(window, text = "Choose an option:").pack(anchor='w')
opt = IntVar(value=1)
tk.Radiobutton(window, text="Encrypt",variable=opt, value=1).pack(anchor='w')
tk.Radiobutton(window, text="Decrypt",variable=opt, value=2).pack(anchor='w')

tk.Label(window, text = "Cipher Shift:").pack(anchor='w')
shift = tk.Entry(window, width=15)
shift.pack(anchor='w')

tk.Label(window, text = "Input text: ").pack(anchor='w')
input = tk.Entry(window, width=40)
input.pack(anchor='w')

output_label = tk.Label(window, text = "")
output_label.pack(anchor='w')

def Caesar_cipher():
    if opt.get() == 1:
        encrypted_text = input.get()
        shift_val = int(shift.get())
        encrypted_text = ''.join(chr((ord(char) + shift_val - 32) % 95 + 32) for char in encrypted_text)
        
        output_label.config(text = "Encrypted Text: " + encrypted_text)
        
    elif opt.get() == 2:
        decrypted_text = input.get()
        shift_val = int(shift.get())
        decrypted_text = ''.join(chr((ord(char) - shift_val - 32) % 95 + 32) for char in decrypted_text)
        
        output_label.config(text = "Decrypted Text: " + decrypted_text)


   

tk.Button(window, text= "Submit", command= Caesar_cipher).pack(anchor='w')


window.mainloop()