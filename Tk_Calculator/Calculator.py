import tkinter as tk
from tkinter import messagebox


def add_digit_button(i):
    return tk.Button(win, text=f"{i}", bg="#FFF5EE", command=lambda: insert_number(i))


def add_operation_button(i):
    return tk.Button(win, text=f"{i}", width=3, bg="#FFD700",
                     font=("Aerial", 11, "bold"),
                     command=lambda: add_operation(i))


def insert_number(digit):
    value = entry.get()
    if value[0:3] == "INF":
        value = value[3:]
    entry.delete(0, "end")
    entry.insert(0, value+f"{digit}")


def delete():
    entry.delete(0, "end")


def add_operation(symbol):
    value = entry.get()
    if value[-1] in "+/*-":
        value = value[:-1]
    else:
        value = eval(value)
    entry.delete(0, "end")
    entry.insert(0, f"{value}" + symbol)


def calculate():
    value = entry.get()
    if value[-1] in "+-*/":
        value = value+value[:-1]
    entry.delete(0, "end")
    try:
        entry.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Warning", "Unknown symbol!!")
        # entry.insert(0, "0")
    except ZeroDivisionError:
        entry.insert(0, "INF")


def press_key(event):
    if event.char.isdigit():
        insert_number(event.char)
    elif event.char in "-+*/":
        add_operation(event.char)
    elif event.char == "\r":
        calculate()


# Window
win = tk.Tk()
win.geometry("240x250")
win.resizable(False, False)
win.config(bg="#000000")
win.bind("<Key>", press_key)
photo = tk.PhotoImage(file="icon.png")
win.iconphoto(False, photo)
# Entry(calculator display)
entry = tk.Entry(win, justify="right", font=("Aerial", 15), border=2, text="0")
entry.grid(row=0, columnspan=4, sticky="wens", padx=5)
win.rowconfigure(0, weight=3)
win.rowconfigure(1, weight=1)
win.rowconfigure(2, weight=1)
win.rowconfigure(3, weight=1)
win.rowconfigure(4, weight=1)

# Operanzi
add_digit_button(1).grid(row=1, column=0, sticky="we", padx=5, pady=3)
add_digit_button(2).grid(row=1, column=1, sticky="we", padx=5, pady=3)
add_digit_button(3).grid(row=1, column=2, sticky="we", padx=5, pady=3)
add_digit_button(4).grid(row=2, column=0, sticky="we", padx=5, pady=3)
add_digit_button(5).grid(row=2, column=1, sticky="we", padx=5, pady=3)
add_digit_button(6).grid(row=2, column=2, sticky="we", padx=5, pady=3)
add_digit_button(7).grid(row=3, column=0, sticky="we", padx=5, pady=3)
add_digit_button(8).grid(row=3, column=1, sticky="we", padx=5, pady=3)
add_digit_button(9).grid(row=3, column=2, sticky="we", padx=5, pady=3)
add_digit_button(0).grid(row=4, column=0, sticky="we", padx=5, pady=3)

# Operatori
add_operation_button("+").grid(row=1, column=3)
add_operation_button("-").grid(row=2, column=3)
add_operation_button("*").grid(row=3, column=3)
add_operation_button("/").grid(row=4, column=3)
equality = tk.Button(win, text="=", bg="red", command=calculate)
equality.grid(row=4, column=2, sticky="wens", padx=7, pady=3)
tk.Button(win, text="C", bg="#FFF5EE", command=delete).grid(row=4, column=1, sticky="we", padx=3)

win.columnconfigure(0, minsize=60)
win.columnconfigure(1, minsize=60)
win.columnconfigure(2, minsize=60)
win.columnconfigure(3, minsize=60)
win.mainloop()
