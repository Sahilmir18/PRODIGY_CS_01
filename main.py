import tkinter as tk


def show_choice():
    
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)

root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x250")

var = tk.IntVar()



tk.Label(root, text="""Choose your options (Decrypy/Encrpyt):""",
         justify=tk.LEFT, padx=20).pack(anchor=tk.W)


R1 = tk.Radiobutton(root, text="Encrypt", variable=var, value=1, command=show_choice)
R1.pack(anchor=tk.W) # anchor=tk.W aligns to the west (left)

R2 = tk.Radiobutton(root, text="Decrypt", variable=var, value=2, command=show_choice)
R2.pack(anchor=tk.W)



# A label to display the current selection
label = tk.Label(root, text="None selected")
label.pack(anchor=tk.W, padx=20, pady=10)


def manipulate_text():
    if var.get() == 1:
        text = entry.get()
        textupper = text.upper()
        def encrypt(textupper):
            translation_table = str.maketrans({
                'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I',
                'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O',
                'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U',
                'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A',
                'Y': 'B', 'Z': 'C'
            })
            encrypted = textupper.translate(translation_table)
            return encrypted
        result = encrypt(textupper)
        result_label.config(text="Encrypted Text: " + result)
    elif var.get() == 2:    
        text = entry.get()
        textupper = text.upper()
        def decrypt(textupper):
            translation_table = str.maketrans({
                'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F',
                'J': 'G', 'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L',
                'P': 'M', 'Q': 'N', 'R': 'O', 'S': 'P', 'T': 'Q', 'U': 'R',
                'V': 'S', 'W': 'T', 'X': 'U', 'Y': 'V', 'Z': 'W', 'A': 'X',
                'B': 'Y',  'C': 'Z'
            })
            decrypted = textupper.translate(translation_table)
            return decrypted
        result = decrypt(textupper)
        result_label.config(text="Decrypted Text: " + result)

    
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Submit", command=manipulate_text)
button.pack(pady=10)

result_label = tk.Label(root, text="", font = ("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
