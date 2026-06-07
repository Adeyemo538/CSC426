import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Calculator")
        self.root.geometry("400x550")

        self.expression = ""
        self.display = tk.Entry(root, font=("Arial", 20), justify="right")
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)

        buttons = [
            ["C", "%", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "\\\\", "="]
        ]

        frame = tk.Frame(root)
        frame.pack(expand=True, fill="both")

        for row in buttons:
            row_frame = tk.Frame(frame)
            row_frame.pack(expand=True, fill="both")
            for btn in row:
                tk.Button(
                    row_frame,
                    text=btn,
                    font=("Arial", 18),
                    command=lambda b=btn: self.click(b)
                ).pack(side="left", expand=True, fill="both")

    def click(self, value):
        if value == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif value == "=":
            try:
                expr = self.expression.replace("^", "**").replace("\\\\", "//")
                result = str(eval(expr))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
        else:
            self.expression += value
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

root = tk.Tk()
Calculator(root)
root.mainloop()
