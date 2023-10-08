import tkinter as tk
from tkinter import messagebox

# Create a function to add a new entry
def add_entry():
    description = description_entry.get()
    amount = amount_entry.get()
    
    if description and amount:
        try:
            amount = float(amount)
            if transaction_type.get() == "Expense":
                expenses_listbox.insert(tk.END, f"Expense: {description} - ${amount:.2f}")
                total_expenses.set(total_expenses.get() + amount)
            elif transaction_type.get() == "Income":
                income_listbox.insert(tk.END, f"Income: {description} + ${amount:.2f}")
                total_income.set(total_income.get() + amount)
            
            description_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
    else:
        messagebox.showerror("Error", "Please enter both description and amount.")

# Create the main application window
app = tk.Tk()
app.title("Expense and Income Tracker")

# Create variables to store the transaction type and totals
transaction_type = tk.StringVar()
transaction_type.set("Expense")
total_expenses = tk.DoubleVar()
total_income = tk.DoubleVar()

# Create labels and entry widgets
description_label = tk.Label(app, text="Description:")
description_label.grid(row=0, column=0)
description_entry = tk.Entry(app)
description_entry.grid(row=0, column=1)

amount_label = tk.Label(app, text="Amount:")
amount_label.grid(row=1, column=0)
amount_entry = tk.Entry(app)
amount_entry.grid(row=1, column=1)

transaction_type_label = tk.Label(app, text="Transaction Type:")
transaction_type_label.grid(row=2, column=0)
transaction_type_menu = tk.OptionMenu(app, transaction_type, "Expense", "Income")
transaction_type_menu.grid(row=2, column=1)

add_button = tk.Button(app, text="Add Entry", command=add_entry)
add_button.grid(row=3, column=0, columnspan=2)

# Create listboxes to display entries
expenses_listbox = tk.Listbox(app, height=10, width=40)
expenses_listbox.grid(row=4, column=0, columnspan=2)
income_listbox = tk.Listbox(app, height=10, width=40)
income_listbox.grid(row=4, column=2, columnspan=2)

# Create labels to display total expenses and income
total_expenses_label = tk.Label(app, text="Total Expenses:")
total_expenses_label.grid(row=5, column=0)
total_expenses_display = tk.Label(app, textvariable=total_expenses)
total_expenses_display.grid(row=5, column=1)

total_income_label = tk.Label(app, text="Total Income:")
total_income_label.grid(row=5, column=2)
total_income_display = tk.Label(app, textvariable=total_income)
total_income_display.grid(row=5, column=3)

# Start the application
app.mainloop()
