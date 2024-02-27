import tkinter as tk
from tkinter import ttk
from tkinter import Label

def binary_to_decimal():
    binary = binary_entry.get()
    decimal = int(binary, 2)
    decimal_label.config(text = f"Decimal: {decimal}")

window = tk.Tk()
window.title("Binary to Decimal")
window.geometry("300x50")

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

window.mainloop()