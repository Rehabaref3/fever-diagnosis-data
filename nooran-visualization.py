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

# Load dataset
df = None
try:
    current_folder = os.path.dirname(__file__)
    file_path = os.path.join(current_folder, "FeverDataset1.csv1")
    df = pd.read_csv(file_path)
    df = df.head(31)
    show_text(f"File read successfully.\nRows loaded: {len(df)}")
except Exception as e:
    show_text(f"Error reading file:\n{e}")

# Function to build figures
def build_figure(fig_num):
    fig = Figure(figsize=(7, 5), dpi=100)
    ax = fig.add_subplot(111)


   # Figure 4: Pareto Chart for Fever Severity
    if fig_num == 4:
        severity_counts = df["Fever_Severity"].value_counts().sort_values(ascending=False)
        cumulative_percent = severity_counts.cumsum() / severity_counts.sum() * 100

        # Create bar chart
        ax.bar(severity_counts.index, severity_counts.values)

        ax.set_title("Pareto Analysis of Fever Severity Levels", fontsize=14, fontweight="bold")
        ax.set_xlabel("Fever Severity")
        ax.set_ylabel("Frequency")
        ax.grid(axis="y", linestyle="--", alpha=0.4)

        # Add value labels on bars
        for i, value in enumerate(severity_counts.values):
            ax.text(i, value + 0.1, str(value), ha="center", fontsize=9)

        # Create secondary axis for cumulative percentage
        ax2 = ax.twinx()
        ax2.plot(severity_counts.index, cumulative_percent.values, marker="o", linewidth=2)
        ax2.set_ylabel("Cumulative Percentage (%)")
        ax2.set_ylim(0, 110)


       # Add percentage labels
        for i, cp in enumerate(cumulative_percent.values):
            ax2.text(i, cp + 2, f"{cp:.1f}%", ha="center", fontsize=8)


