import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Enhanced Calculator")

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entry field for the result
        self.result_entry = tk.Entry(self.master, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_value = 1
        col_value = 0

        for button in buttons:
            tk.Button(self.master, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: self.on_button_click(b)).grid(row=row_value, column=col_value)
            col_value += 1
            if col_value > 3:
                col_value = 0
                row_value += 1

        # Clear button
        tk.Button(self.master, text='C', padx=20, pady=20, font=("Arial", 18), command=self.clear).grid(row=row_value, column=0)

        # Bind keyboard events
        self.master.bind('<Return>', lambda event: self.on_button_click('='))
        self.master.bind('<BackSpace>', lambda event: self.clear())

        for i in range(10):
            self.master.bind(str(i), lambda event, num=i: self.on_button_click(str(num)))
        self.master.bind('.', lambda event: self.on_button_click('.'))
        self.master.bind('+', lambda event: self.on_button_click('+'))
        self.master.bind('-', lambda event: self.on_button_click('-'))
        self.master.bind('*', lambda event: self.on_button_click('*'))
        self.master.bind('/', lambda event: self.on_button_click('/'))

    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)  # Evaluate the expression
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif char == 'C':
            self.clear()
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()