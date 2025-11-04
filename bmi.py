import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x370")
root.configure(bg="#f0f4c3")

# Title Label
title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 20, "bold"), bg="#f0f4c3")
title_label.pack(pady=20)

# Frame for Inputs
input_frame = tk.Frame(root, bg="#f0f4c3")
input_frame.pack(pady=10)

# Weight Input
weight_label = tk.Label(input_frame, text="Weight (kg):", font=("Arial", 12), bg="#f0f4c3")
weight_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
weight_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

# Height Input
height_label = tk.Label(input_frame, text="Height (m):", font=("Arial", 12), bg="#f0f4c3")
height_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
height_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
height_entry.grid(row=1, column=1, padx=5, pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f4c3")
result_label.pack(pady=30)

# Calculate BMI Function
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Must be positive numbers.")

        bmi = weight / (height ** 2)
        if bmi < 18.5:
            status = "Underweight"
            colour = "#1565c0"
        elif 18.5 <= bmi < 25:
            status = "Normal Weight"
            colour = "#388e3c"
        elif 25 <= bmi < 30:
            status = "Overweight"
            colour = "#fbc02d"
        else:
            status = "Obesity"
            colour = "#c62828"
        result_label.config(text=f"BMI: {bmi:.2f}\nStatus: {status}", fg=colour)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter positive numbers for weight and height.")

# Reset Function
def reset():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

# Button Frame
button_frame = tk.Frame(root, bg="#f0f4c3")
button_frame.pack(pady=5)

calculate_btn = tk.Button(button_frame, text="Calculate BMI", command=calculate_bmi,
                         font=("Arial", 12), bg="#4caf50", fg="black", width=14)
calculate_btn.grid(row=0, column=0, padx=12, pady=10)

reset_btn = tk.Button(button_frame, text="Reset", command=reset,
                     font=("Arial", 12), bg="#f44336", fg="black", width=14)
reset_btn.grid(row=0, column=1, padx=12, pady=10)

# Run the app
root.mainloop()
