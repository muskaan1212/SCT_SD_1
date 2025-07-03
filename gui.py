import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        input_unit = combo_from.get()
        output_unit = combo_to.get()

        if input_unit == output_unit:
            result = temp
        elif input_unit == "Celsius":
            if output_unit == "Fahrenheit":
                result = (temp * 9/5) + 32
            elif output_unit == "Kelvin":
                result = temp + 273.15
        elif input_unit == "Fahrenheit":
            if output_unit == "Celsius":
                result = (temp - 32) * 5/9
            elif output_unit == "Kelvin":
                result = (temp - 32) * 5/9 + 273.15
        elif input_unit == "Kelvin":
            if output_unit == "Celsius":
                result = temp - 273.15
            elif output_unit == "Fahrenheit":
                result = (temp - 273.15) * 9/5 + 32

        label_result.config(text=f"Result: {round(result, 2)} {output_unit}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("🌡️ Temperature Converter")
root.geometry("350x250")
root.resizable(False, False)

# Input temperature
label_temp = tk.Label(root, text="Enter Temperature:")
label_temp.pack(pady=5)
entry_temp = tk.Entry(root)
entry_temp.pack(pady=5)

# From unit
label_from = tk.Label(root, text="From:")
label_from.pack(pady=5)
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_from.current(0)
combo_from.pack(pady=5)

# To unit
label_to = tk.Label(root, text="To:")
label_to.pack(pady=5)
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_to.current(1)
combo_to.pack(pady=5)

# Convert button
btn_convert = tk.Button(root, text="Convert", command=convert_temperature)
btn_convert.pack(pady=10)

# Result
label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=5)

root.mainloop()
