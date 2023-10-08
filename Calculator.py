import tkinter as tk

# Function to perform arithmetic operation
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry field for input
entry = tk.Entry(root, width=25, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Buttons for calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text='C', padx=20, pady=20, font=("Arial", 20), command=lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val)

# Equal button
tk.Button(root, text='=', padx=20, pady=20, font=("Arial", 20), command=calculate).grid(row=row_val, column=col_val + 1)

# Run the main loop
root.mainloop()
 
