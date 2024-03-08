import tkinter as tk
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def clear():
    entry.delete(0, tk.END)
def insert_value(value):
    entry.insert(tk.END, value)

def backspace():
    entry.delete(len(entry.get()) - 1)

root = tk.Tk()
root.title("Simple Calculator")
entry = tk.Entry(root, width=20, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('00', 4, 1), ('.', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    b = tk.Button(root, text=text, width=9, height=2,
                  command=lambda t=text: insert_value(t))
    b.grid(row=row, column=col)

clear_button = tk.Button(root, text='C', width=19, height=2,command=clear)
clear_button.grid(row=5, column=0, columnspan=2)
backspace_button = tk.Button(root, text='⌫', width=9, height=2, command=backspace)
backspace_button.grid(row=5, column=2)
evaluate_button = tk.Button(root, text='=', width=9, height=2,command=evaluate_expression)
evaluate_button.grid(row=5, column=3)
root.mainloop()
