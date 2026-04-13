import os
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create the main application window
root = tk.Tk()
root.title("Fever Dataset Dashboard")
root.geometry("560x560")

# Add the main title
title = tk.Label(root, text="Fever Dataset Dashboard", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Create a text box for written output messages
text_box = tk.Text(root, height=10, width=62)
text_box.pack(pady=15)

# Function to display messages in the output box
def show_text(msg):
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, msg)
    print(msg)
    print("-" * 50)

# Initialize dataset variable
df = None

try:
    # Get the current folder where the Python file exists
    current_folder = os.path.dirname(__file__)

    # Build the full path of the CSV file
    file_path = os.path.join(current_folder, "FeverDataset1.csv")

    # Read the dataset
    df = pd.read_csv(file_path)

    # Select only the first 31 rows
    df = df.head(31)

    # Show success output message
    show_text(f"File read successfully.\nRows loaded: {len(df)}")

except Exception as e:
    # Show error output message if file reading fails
    show_text(f"Error reading file:\n{e}")

# Function to build each figure based on figure number
def build_figure(fig_num):
    fig = Figure(figsize=(7, 5), dpi=100)
    ax = fig.add_subplot(111)

    # Figure 1: Pie chart for Previous Medication
    if fig_num == 1:
        # Define custom colors: Purple, Pink, Blue
        custom_colors = ["#a063b8", "#cc4a78", "#5fa8df"]

        df["Previous_Medication"].value_counts().plot(
            kind="pie",
            autopct=lambda pct: f'{pct:.1f}% ({int(round(pct * sum(df["Previous_Medication"].value_counts()) / 100.0))})',
            startangle=90,
            ax=ax,
            colors=custom_colors
        )
        ax.set_title("Previous Medication Distribution")
        ax.set_ylabel("")
        ax.text(
            0.5,
            -0.05,
            "Percentage = Medication Distribution | ( ) = Number of Patients",
            transform=ax.transAxes,
            ha="center",
            fontsize=9,
            style="italic"
        )
        
# Graph 2: Age Distribution (Histogram)
elif fig_num == 2:

    # Create a histogram to show the distribution of ages
    df["Age"].plot(
        kind="hist",              # Define plot type as histogram
        bins=10,                  # Divide data into 10 intervals (bins)
        color="#6c5ce7",          # Set bar color
        edgecolor="white",        # Add borders to bars
        linewidth=1.2,            # Thickness of bar edges
        rwidth=0.9,               # Width of bars (adds spacing between them)
        alpha=0.85,               # Transparency level
        ax=ax                     # Draw plot on the given axis
    )

    # Set chart title with styling
    ax.set_title("Age Distribution of Patients", fontsize=14, fontweight="bold", pad=15)

    # Label for X-axis
    ax.set_xlabel("Age", fontsize=12)

    # Label for Y-axis (frequency of patients in each age group)
    ax.set_ylabel("Frequency (Number of Patients)", fontsize=12)

    # Add horizontal grid lines for better readability
    ax.grid(axis="y", linestyle="--", alpha=0.3)

    # Remove top border for cleaner appearance
    ax.spines["top"].set_visible(False)

    # Remove right border for cleaner appearance
    ax.spines["right"].set_visible(False)


# Graph 3: Age vs Heart Rate (LINE GRAPH)
elif fig_num == 3:

    # Sort data by Age to make the line plot meaningful
    sorted_df = df.sort_values(by="Age")

    # Create a line plot showing relationship between Age and Heart Rate
    ax.plot(
        sorted_df["Age"],         # X-axis values (Age)
        sorted_df["Heart_Rate"],  # Y-axis values (Heart Rate)
        marker="o",               # Show points on the line
        linewidth=3,              # Thickness of the line
        color="#e74c3c"           # Line color
    )

    # Set chart title
    ax.set_title("Age vs Heart Rate")

    # Label X-axis
    ax.set_xlabel("Age")

    # Label Y-axis
    ax.set_ylabel("Heart Rate")

    # Add grid for better visualization
    ax.grid(True)
