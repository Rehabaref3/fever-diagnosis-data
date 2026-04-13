import os #Used to handle file paths
import pandas as pd # Used tp read and process the dataset
import tkinter as tk   # GUI library for creating the dashboard window
from matplotlib.figure import Figure # Used to create plots
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Embeds plots into Tkinter

# Improved visualisations using the same dataset variables
# Create main application window

root = tk.Tk()
root.title("Improved Visualisation Dashboard")
root.geometry("560x420")

title = tk.Label(root, text="Improved Visualisation Dashboard", font=("Arial", 16, "bold"))
title.pack(pady=12)

text_box = tk.Text(root, height=7, width=60)
text_box.pack(pady=10)

# Function to display messages
def show_text(msg):
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, msg)
    print(msg)
    print("-" * 50)
