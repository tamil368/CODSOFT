import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        choice = operation_var.get()
        
        if choice == '+':
            c = a + b
        elif choice == '-':
            c = a - b
        elif choice == '*':
            c = a * b
        elif choice == '%':
            c = a / b
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        result_var.set(f"Answer = {c}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Enter the A number:").grid(row=0, column=0, padx=10, pady=10)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the B number:").grid(row=1, column=0, padx=10, pady=10)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Operations (+, -, *, %):").grid(row=2, column=0, padx=10, pady=10)
operation_var = tk.StringVar()
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "%")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2, pady=20)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=4, columnspan=2, pady=10)

root.mainloop()
