
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
            colors=custom_colors      # Added custom colors
        )
        ax.set_title("Previous Medication Distribution")
        ax.set_ylabel("")
        ax.text(0.5, -0.05, "Percentage = Medication Distribution | ( ) = Number of Patients", 
        transform=ax.transAxes, ha='center', fontsize=9, style='italic')   # Text below chart: % = medication, ( ) = patient count

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


#This part was implemented by Nooran
#includes :
#graph 4, 
#graph 5


    # Figure 4: Horizontal bar chart for Fever Severity
    # This graph shows the frequency of each fever severity category.
    elif fig_num == 4:
        df["Fever_Severity"].value_counts().plot(  # Count each severity level and plot the results.
            kind="barh",  # Use a horizontal bar chart for clearer category comparison.
            ax=ax  # Draw the graph inside the current figure window.
        )
        ax.set_title("Fever Severity Levels")  # Set the graph title.
        ax.set_xlabel("Count")  # Label the x-axis as count.
        ax.set_ylabel("Severity")  # Label the y-axis as severity category.

    # Figure 5: Box plot for Heart Rate by Fever Severity
    # This graph compares heart rate distribution across fever severity levels.
    elif fig_num == 5:
        box = df.boxplot(
            column="Heart_Rate",  # Select Heart_Rate as the numerical variable.
            by="Fever_Severity",  # Group the values by fever severity.
            ax=ax,  # Draw the box plot inside the current figure window.
            patch_artist=True,  # Enable box filling with colors.
            boxprops=dict(linewidth=2),  # Make box borders clearer.
            medianprops=dict(color='#d63031', linewidth=3),  # Highlight the median line.
            whiskerprops=dict(linewidth=2),  # Make whiskers more visible.
            capprops=dict(linewidth=2)  # Make caps more visible.
        )

        colors = ['#74b9ff', '#55efc4', '#ffeaa7', '#ff7675', '#a29bfe']  # Define fill colors for boxes.
        for patch, color in zip(ax.patches, colors):
            patch.set_facecolor(color)  # Apply a color to each box.

        ax.set_title("Heart Rate Distribution by Fever Severity")  # Set the graph title.
        fig.suptitle("")  # Remove the automatic extra title.
        ax.set_xlabel("Fever Severity")  # Label the x-axis.
        ax.set_ylabel("Heart Rate")  # Label the y-axis.
        ax.grid(True)  # Add grid lines for readability.

    return fig  # Return the completed figure.

# Function to open a new window for each graph
def open_graph_window(fig_num):
    # Stop if the dataset is not loaded
    if df is None:
        show_text("Dataset not loaded.")
        return

    # Display a short success message for each selected figure
    if fig_num == 1:
        show_text("Figure 1 opened successfully.\nPie chart for Previous Medication was generated.")
    elif fig_num == 2:
        show_text("Figure 2 opened successfully.\nHistogram for Age Distribution was generated.")
    elif fig_num == 3:
        show_text("Figure 3 opened successfully.\nLine graph for Age vs Heart Rate was generated.")
    elif fig_num == 4:
        show_text("Figure 4 opened successfully.\nBar chart for Fever Severity was generated.")
    elif fig_num == 5:
        show_text("Figure 5 opened successfully.\nBox plot for Heart Rate by Fever Severity was generated.")

    # Create a new graph window
    win = tk.Toplevel(root)
    win.title(f"Figure {fig_num}")
    win.geometry("750x650")

    # Build and display the selected figure
    fig = build_figure(fig_num)
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Create a frame for graph control buttons
    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)

    # Add a button to move to the next figure
    if fig_num < 5:
        tk.Button(
            btn_frame,
            text="Next Figure",
            command=lambda: [win.destroy(), open_graph_window(fig_num + 1)]
        ).pack(side="left", padx=10)

    # Add a button to close the current graph window
    tk.Button(
        btn_frame,
        text="Close",
        command=win.destroy
    ).pack(side="left", padx=10)

# Create dashboard buttons for opening each figure
tk.Button(root, text="Figure 1", command=lambda: open_graph_window(1), width=30).pack(pady=5)
tk.Button(root, text="Figure 2", command=lambda: open_graph_window(2), width=30).pack(pady=5)
tk.Button(root, text="Figure 3", command=lambda: open_graph_window(3), width=30).pack(pady=5)
tk.Button(root, text="Figure 4", command=lambda: open_graph_window(4), width=30).pack(pady=5)
tk.Button(root, text="Figure 5", command=lambda: open_graph_window(5), width=30).pack(pady=5)

# Add an Exit button to close the dashboard
tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", width=30).pack(pady=15)

# Run the application
root.mainloop()