# Implemented by Leen
# ================================
# Import Libraries
# ================================

import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk


# ================================
# Sample Data
# ================================

data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 30, 25, 40],
    "Heart_Rate": [72, 75, 78, 80, 85, 88, 90, 77, 74, 82]
}

df = pd.DataFrame(data)


# ================================
# Graph 1: Age Distribution (Pie Chart)
# ================================

def show_age_pie():
    plt.figure(figsize=(7, 7))

    age_counts = df["Age"].value_counts()

    plt.pie(
        age_counts,
        labels=age_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.Paired.colors
    )

    plt.title("Age Distribution of Patients (Pie Chart)")
    plt.tight_layout()
    plt.show()


# ================================
# Graph 2: Heart Rate vs Age (Bar Chart - Original)
# ================================

def show_heart_rate_bar():
    plt.figure(figsize=(9, 5))

    plt.bar(
        df["Age"].astype(str),
        df["Heart_Rate"],
        color='#e74c3c',
        alpha=0.8
    )

    plt.title("Age vs Heart Rate (Bar Chart)")
    plt.xlabel("Age")
    plt.ylabel("Heart Rate")

    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.show()


# ================================
# UI Window (Tkinter)
# ================================

root = tk.Tk()
root.title("Health Data Visualization")
root.geometry("400x250")


label = tk.Label(root, text="Select Graph", font=("Arial", 14))
label.pack(pady=20)


btn1 = tk.Button(root, text="Age Distribution (Pie)", command=show_age_pie, width=30)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Heart Rate (Bar Chart)", command=show_heart_rate_bar, width=30)
btn2.pack(pady=10)


root.mainloop()
