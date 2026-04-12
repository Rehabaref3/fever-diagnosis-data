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


#This part was implemented by Nooran:
# Figure 4: Horizontal bar chart for Fever Severity
# Figure 5: Box plot for Heart Rate by Fever Severity

# Figure 4: Fever Severity Levels
# This figure is designed to visualize how frequently each fever severity category appears in the dataset.
plt.figure(figsize=(8,5))  # Create a new figure window with a suitable size to make the chart clear and readable.

df["Fever_Severity"].value_counts().plot(  # Count the number of occurrences for each fever severity category, then prepare it for plotting.
    kind="barh",  # Use a horizontal bar chart because it makes category names easier to read and compare visually.
    color=['#ff7675','#fdcb6e','#55efc4'])  # Apply custom colors to make the categories visually distinct and improve presentation quality.

plt.title("Fever Severity Levels")  # Add a title to clearly describe what this graph is showing.
plt.xlabel("Count")  # Label the x-axis to indicate that it represents the number of records or patients.
plt.ylabel("Severity")  # Label the y-axis to indicate that it contains the fever severity categories.
plt.show()  # Display the completed graph to the user.



# Figure 5: Heart Rate by Fever Severity (Styled Box Plot)
# This figure is created to compare heart rate distribution across different fever severity groups.
box = df.boxplot(  # Generate a box plot from the dataset for grouped statistical comparison.
    column="Heart_Rate",  # Select the Heart_Rate column as the numerical variable to be analyzed.
    by="Fever_Severity",  # Group the heart rate values according to fever severity categories.
    patch_artist=True,  # Enable colored filling inside the boxes to improve the visual appearance of the plot.
    boxprops=dict(linewidth=2),  # Increase the thickness of the box borders so they appear more clearly.
    medianprops=dict(color='#d63031', linewidth=3),  # Highlight the median line using a stronger color and thicker width for emphasis.
    whiskerprops=dict(linewidth=2),  # Make the whisker lines thicker for clearer visibility.
    capprops=dict(linewidth=2)  # Make the cap lines at the ends of whiskers thicker for a more polished result.
)

colors = ['#74b9ff', '#55efc4', '#ffeaa7', '#ff7675', '#a29bfe']  # Create a list of colors to style the box plot categories.
for patch, color in zip(box.artists, colors):  # Loop through each box in the chart and assign a color to it.
    patch.set_facecolor(color)  # Fill each box with its corresponding color to improve distinction between groups.

plt.title("Heart Rate Distribution by Fever Severity", fontsize=15, fontweight="bold")  # Add a bold and descriptive title to explain the graph clearly.
plt.suptitle("")  # Remove the automatic extra title generated by pandas to keep the chart cleaner.
plt.xlabel("Fever Severity")  # Label the x-axis to show that each box belongs to a fever severity category.
plt.ylabel("Heart Rate")  # Label the y-axis to show that the measured values represent heart rate.
plt.grid(True, linestyle='--', alpha=0.5)  # Add a light dashed grid to make the graph easier to read and interpret.
plt.show()  # Display the final styled box plot to the user


# Function to open a new window for each graph
def open_graph_window(fig_num):
    # Stop if the dataset was not loaded
    if df is None:
        show_text("Dataset not loaded.")
        return

    # Show written output for each figure
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

    
    win = tk.Toplevel(root)
    win.title(f"Figure {fig_num}")
    win.geometry("750x650")

  # Create and display the selected figure
    fig = build_figure(fig_num)
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Create a frame for navigation buttons
    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)

    # Add Next Figure button if this is not the last figure
    if fig_num < 5:
        tk.Button(
            btn_frame,
            text="Next Figure",
            command=lambda: [win.destroy(), open_graph_window(fig_num + 1)]
        ).pack(side="left", padx=10)

    # Add Close button
    tk.Button(
        btn_frame,
        text="Close",
        command=win.destroy
    ).pack(side="left", padx=10)

# Create buttons in the main dashboard
tk.Button(root, text="Figure 1", command=lambda: open_graph_window(1), width=30).pack(pady=5)
tk.Button(root, text="Figure 2", command=lambda: open_graph_window(2), width=30).pack(pady=5)
tk.Button(root, text="Figure 3", command=lambda: open_graph_window(3), width=30).pack(pady=5)
tk.Button(root, text="Figure 4", command=lambda: open_graph_window(4), width=30).pack(pady=5)
tk.Button(root, text="Figure 5", command=lambda: open_graph_window(5), width=30).pack(pady=5)

# Add Exit button to close the whole application
tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", width=30).pack(pady=15)

# Start the application
root.mainloop()

