

import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
# import time



def open_file():
    """Redaktirlemek ucin fayl acmagyn kody"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"TM_söz paneli - {filepath}")

def save_file():
    """Häzirki faýly täze faýl görnüşinde ýatda saklatmak uçin."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"TM_söz paneli - {filepath}")

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

# top = tk.Tk()
window = tk.Tk()
window.title("TM_söz paneli.v1")
# top.geometry("450x450")
# top.eval('tk::PlaceWindow . center')
window.geometry("1500x750")
window.config(bg=rgb_hack((255, 0, 122)))
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
# windowWhidth = root.winfo_reqwidth()
# windowHeight = root.winfo_reqheight()




""" Ilki acylyan login parol paneli"""
# def fun():
#     messagebox.showinfo()

# user_name = Label(top,
# 				text = "Username").place(x = 40,
# 										y = 60)

# user_password = Label(top,
# 					text = "Password").place(x = 40,
											# y = 100)
                                            # activeforeground = "blue",
                                            # activebackground = "pink",
                                            # pady = 10)

# submit_button = Button(top,
# 					text = "Submit").place(x = 40,
# 											y = 130)

# user_name_input_area = Entry(top,
# 							width = 30).place(x = 110,
# 											y = 60)

# user_password_entry_area = Entry(top,
# 								width = 30).place(x = 110,
# 												y = 100)

txt_edit = tk.Text(window,
                width=25,
                height = 8,
                font = ('Times' , 20),
                wrap = 'word',
                fg = '#4A7A8C')
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Açmak", command=open_file)
btn_save = tk.Button(frm_buttons, text="Ýatda sakla...", command=save_file)
btn_save_as = tk.Button(frm_buttons, text="Täzeden Ýatda sakla...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_save_as.grid(row=2, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
window.mainloop()