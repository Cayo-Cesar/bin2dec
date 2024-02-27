import tkinter as tk
from tkinter import ttk
from tkinter import Label

def binary_to_decimal():
    try:
        binary = binary_entry.get()
        decimal = int(binary, 2)
        decimal_label.config(text = f"Decimal: {decimal}")
    except ValueError:
        decimal_label.config(text = "Invalid input")

def decimal_to_binary():
    try:
        decimal = int(decimal_entry.get())
        binary = bin(decimal)[2:]  
        binary_label.config(text = f"Binary: {binary}")
    except ValueError:
        binary_label.config(text = "Invalid input")

window = tk.Tk()
window.title("Binary to Decimal")
window.geometry("300x150")

# Create a label
binary_label = Label(window, text = "Binary: ")
binary_label.grid(column = 0, row = 0)

# Create a text entry
binary_entry = ttk.Entry(window)
binary_entry.grid(column = 1, row = 0)

# Create a button
binary_button = ttk.Button(window, text = "Converter", command = binary_to_decimal)
binary_button.grid(column = 2, row = 0)

# Create a label
decimal_label = Label(window, text = "Decimal: ")
decimal_label.grid(column = 0, row = 1)

# Create a label for displaying the results
result_label = Label(window, text="")
result_label.grid(column=0, row=2, columnspan=3)

# Create a label
decimal_label1 = Label(window, text = "Decimal: ")
decimal_label1.grid(column = 0, row = 3)

# Create a text entry
decimal_entry = ttk.Entry(window)
decimal_entry.grid(column = 1, row = 3)

# Create a button
decimal_button = ttk.Button(window, text = "Converter", command = decimal_to_binary)
decimal_button.grid(column = 2, row = 3)

# Create a label
binary_label = Label(window, text = "Binary: ")
binary_label.grid(column = 0, row = 4)

# Create a label for displaying the results
result_label = Label(window, text="")
result_label.grid(column=3, row=5, columnspan=3)

window.mainloop()