# calculator_app.py
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")

        self.equation = tk.StringVar()
        self.entry_value = ""

        self.create_widgets()

    def create_widgets(self):
        # Create the entry box for displaying equations
        entry = tk.Entry(self.root, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_value = 1
        col_value = 0
        for button in buttons:
            action = lambda x=button: self.click(x)
            if button == '=':
                tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18), bg="lightblue", command=action).grid(row=row_value, column=col_value, columnspan=4, sticky="nsew")
            else:
                tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_value, column=col_value, sticky="nsew")
            
            col_value += 1
            if col_value > 3:
                col_value = 0
                row_value += 1

    def click(self, item):
        current_equation = str(self.equation.get())
        if item == "=":
            try:
                result = str(eval(current_equation))
                self.equation.set(result)
            except Exception as e:
                self.equation.set("Error")
                messagebox.showerror("Error", "Invalid Input")
        else:
            self.entry_value = current_equation + str(item)
            self.equation.set(self.entry_value)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
