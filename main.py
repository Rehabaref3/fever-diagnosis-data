import os
import pandas as pd
import tkinter as tk
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
        df["Previous_Medication"].value_counts().plot(
            kind="pie",
            autopct='%1.1f%%',
            startangle=90,
            ax=ax
        )
        ax.set_title("Previous Medication Distribution")
        ax.set_ylabel("")

#Implemented by Leen 
#Includes:
#Graph 2: Age distribution
#Graph 3: Age vs heart rate 

# Graph 2: Age Distribution (Histogram)
plt.figure(figsize=(9, 6))

df["Age"].plot(
    kind="hist",
    bins=10,
    color="#6c5ce7",
    edgecolor="white",
    linewidth=1.2,
    rwidth=0.9,
    alpha=0.85
)
plt.title("Age Distribution of Patients", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency (Number of Patients)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.show()



# Graph 3: Age vs Heart Rate (LINE GRAPH)
sorted_df = df.sort_values(by="Age")
plt.figure(figsize=(8,5))
plt.plot(sorted_df["Age"], sorted_df["Heart_Rate"],
         marker='o',
         linewidth=3,
         color='#e74c3c')

plt.title("Age vs Heart Rate")
plt.xlabel("Age")
plt.ylabel("Heart Rate")
plt.grid(True)
plt.show()


#This part was implemented by Nooran:
# Figure 4: Horizontal bar chart for Fever Severity
# Figure 5: Box plot for Heart Rate by Fever Severity


# Figure 4: Fever Severity Levels
    elif fig_num == 4:
        df["Fever_Severity"].value_counts().plot(
            kind="barh",
            color=['#ff7675', '#fdcb6e', '#55efc4'],
            ax=ax
        )
        ax.set_title("Fever Severity Levels")
        ax.set_xlabel("Count")
        ax.set_ylabel("Severity")

    # Figure 5: Heart Rate by Fever Severity (Styled Box Plot)
    elif fig_num == 5:
        box = df.boxplot(
            column="Heart_Rate",
            by="Fever_Severity",
            patch_artist=True,
            ax=ax,
            boxprops=dict(linewidth=2),
            medianprops=dict(color='#d63031', linewidth=3),
            whiskerprops=dict(linewidth=2),
            capprops=dict(linewidth=2)
        )

        colors = ['#74b9ff', '#55efc4', '#ffeaa7', '#ff7675', '#a29bfe']
        for patch, color in zip(box.artists, colors):
            patch.set_facecolor(color)

        ax.set_title("Heart Rate Distribution by Fever Severity", fontsize=15, fontweight="bold")
        fig.suptitle("")
        ax.set_xlabel("Fever Severity")
        ax.set_ylabel("Heart Rate")
        ax.grid(True, linestyle='--', alpha=0.5)
