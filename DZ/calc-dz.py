import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.buttons = []
        for i in range(10):
            button = tk.Button(master, text=str(i), command=lambda x=i: self.update_display(str(x)))
            button.grid(row=(9-i)//3+1, column=(i%3), padx=5, pady=5)
            self.buttons.append(button)
        self.operator_buttons = []
        operators = ["+", "-", "*", "/", "=", "C"]
        for i, operator in enumerate(operators):
            button = tk.Button(master, text=operator, command=lambda x=operator: self.handle_operator(x))
            button.grid(row=i+1, column=3, padx=5, pady=5)
            self.operator_buttons.append(button)
        self.current_number = ""
        self.operator = None
        self.result = 0

    def update_display(self, value):
        self.current_number += value
        self.result_label.config(text=self.current_number)

    def handle_operator(self, operator):
        if operator == "C":
            self.current_number = ""
            self.operator = None
            self.result = 0
            self.result_label.config(text="")
        elif operator == "=":
            if self.operator == "+":
                self.result += float(self.current_number)
            elif self.operator == "-":
                self.result -= float(self.current_number)
            elif self.operator == "*":
                self.result *= float(self.current_number)
            elif self.operator == "/":
                self.result /= float(self.current_number)
            self.current_number = str(self.result)
            self.operator = None
            self.result = 0
            self.result_label.config(text=self.current_number)
        else:
            self.operator = operator
            self.result += float(self.current_number)
            self.current_number = ""
            self.result_label.config(text="")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
