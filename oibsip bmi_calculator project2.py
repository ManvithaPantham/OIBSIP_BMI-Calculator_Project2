import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# In-memory data storage
bmi_records = []

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        
        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Error", "Enter positive numbers for weight and height.")
            return
        
        # Convert height from cm to meters
        height_m = height_cm / 100  
        
        bmi = round(weight / (height_m ** 2), 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
        
        result_label.config(text=f"Your BMI is {bmi} ({category})")
        
        # Save record
        bmi_records.append(bmi)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def show_history():
    if not bmi_records:
        messagebox.showinfo("No Data", "No BMI records available.")
        return
    plt.plot(bmi_records, marker="o", color="blue")
    plt.title("BMI History")
    plt.xlabel("Attempt")
    plt.ylabel("BMI")
    plt.show()

# GUI Window
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Height (cm):").grid(row=1, column=0, padx=10, pady=5)

weight_entry = tk.Entry(root)
height_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)
height_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(root, text="Show History", command=show_history).grid(row=3, column=0, columnspan=2, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
