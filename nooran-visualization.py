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
def show_text(msg):
    text_box.delete("1.0", tk.END)  # Clear previous text
    text_box.insert(tk.END, msg)  # Insert new message
    print(msg)  # Print to console for debugging
    print("-" * 50)
    
    df = None  # Initialize dataset variable globally
    try:
    current_folder = os.path.dirname(__file__) # Get current script directory
    file_path = os.path.join(current_folder, "FeverDataset1.csv")  # Build full file path
    df = pd.read_csv(file_path)
    df = df.head(31)
    show_text(f"File read successfully.\nRows loaded: {len(df)}")
except Exception as e:
    show_text(f"Error reading file:\n{e}") # Display error message

# Function to build different figures based on figure number
def build_figure(fig_num): # Create figure object
    fig = Figure(figsize=(7, 5), dpi=100)
    ax = fig.add_subplot(111) # Add subplot


   # Figure 4: Pareto Chart for Fever Severity
    if fig_num == 4:
          # Count frequency of each severity level
        severity_counts = df["Fever_Severity"].value_counts().sort_values(ascending=False)
         # Calculate cumulative percentage for Pareto analysis
        cumulative_percent = severity_counts.cumsum() / severity_counts.sum() * 100
        
         # Create bar chart
ax.bar(severity_counts.index, severity_counts.values)

        ax.set_title("Pareto Analysis of Fever Severity Levels", fontsize=14, fontweight="bold")
        ax.set_xlabel("Fever Severity")
        ax.set_ylabel("Frequency")
        ax.grid(axis="y", linestyle="--", alpha=0.4)

  # Add value labels on bars
# This improves readability by allowing users to see exact frequencies
        # without estimating from the y-axis (enhances data transparency)
for i, value in enumerate(severity_counts.values):
            ax.text(i, value + 0.1, str(value), ha="center", fontsize=9)
    
   # Create secondary axis for cumulative percentage
        # A second axis is used to combine two related metrics (frequency + cumulative %)
        # which is a key feature of a Pareto chart (supports decision-making analysis)
  ax2 = ax.twinx()
        ax2.plot(severity_counts.index, cumulative_percent.values, marker="o", linewidth=2)
        ax2.set_ylabel("Cumulative Percentage (%)")
        ax2.set_ylim(0, 110)

 # Add percentage labels
        # Displaying cumulative percentages helps identify the 80/20 rule visually
        for i, cp in enumerate(cumulative_percent.values):
            ax2.text(i, cp + 2, f"{cp:.1f}%", ha="center", fontsize=8)

  # Figure 5: Box Plot with Raw Data Points
    elif fig_num == 5:
        # Extract and sort severity levels to ensure consistent ordering in the plot
        # Sorting improves interpretability and avoids random category placement

        severity_order = sorted(df["Fever_Severity"].dropna().unique())

        # Group heart rate data by severity level
        # This enables comparison of distributions across categories
 grouped_data = [
            df[df["Fever_Severity"] == level]["Heart_Rate"].dropna()
            for level in severity_order
        ]

 # Define colors for better visual distinction
        # Colour coding improves user experience and reduces cognitive load
        colors = ["skyblue", "lightgreen", "salmon", "plum", "khaki"]

   # Create boxplot
        # Boxplots summarise distribution (median, quartiles, outliers)
        # making them suitable for statistical comparison
        bp = ax.boxplot(
            grouped_data,
            patch_artist=True,  # Enables custom colouring (improves aesthetics)
            labels=severity_order,
            widths=0.5
        )

   # Apply colors to each box
        # Transparency is used to prevent visual clutter when overlaying data points
        for box, color in zip(bp["boxes"], colors):
            box.set_facecolor(color)
            box.set_alpha(0.35) # Semi-transparent for layering effect
            box.set_edgecolor("black") # Semi-transparent for layering effecty

   # Overlay raw data points (jittered to avoid overlap)
        # Adding raw data improves accuracy and avoids hiding data distribution
        # Jittering prevents points from stacking on top of each other
 for i, (group, color) in enumerate(zip(grouped_data, colors), start=1):
            jittered_x = [i + ((j - len(group)/2) * 0.02) for j in range(len(group))]
            ax.scatter(jittered_x, group, alpha=0.8, s=25, color=color, edgecolors="black", linewidths=0.3)

          # Display mean value for additional statistical insight
            # Mean complements median shown in boxplot for deeper analysis
            mean_value = group.mean()
            ax.text(i + 0.05, mean_value, f"{mean_value:.1f}", fontsize=8)

# Labels and title
        # Clear labelling ensures the graph is self-explanatory (important for reports)
ax.set_title("Heart Rate Distribution by Fever Severity")
        ax.set_xlabel("Fever Severity")
        ax.set_ylabel("Heart Rate")
        ax.grid(axis="y", linestyle="--", alpha=0.4)  # Gridlines improve readability

    return fig  # Return the generated figure for embedding in GUI

# Function to open graph in a new window
def open_graph(fig_num):
     # Validation check to prevent runtime errors if dataset failed to load
    if df is None:
        show_text("Dataset not loaded.") # User-friendly error message
        return
def open_graph(fig_num):
    if df is None:
        show_text("Dataset not loaded.")
        return
           # Display status message
    # Provides feedback to improve interactivity and usability
 if fig_num == 4:
        show_text("Figure 4 opened successfully.\nImproved Cleveland dot plot was generated.")
    elif fig_num == 5:
        show_text("Figure 5 opened successfully.\nImproved box plot with raw data points was generated.")

        
    # Create new window for graph
    # Using a separate window improves UI organisation and avoids clutter
        = tk.Toplevel(root)
    win.title(f"Figure {fig_num}")
    win.geometry("800x650")  # Larger size for better data visibility

# Build and display figure
    # Embedding Matplotlib in Tkinter allows integration of analysis + GUI
    fig = build_figure(fig_num)
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)

    fig = build_figure(fig_num)
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)


    if fig_num == 4:
        tk.Button(btn_frame, text="Next Figure", width=15,
                  command=lambda: [win.destroy(), open_graph(5)]).pack(side="left", padx=10)
tk.Button(root, text="Open Figure 4", width=25, height=2, command=lambda: open_graph(4)).pack(pady=8)
tk.Button(root, text="Open Figure 5", width=25, height=2, command=lambda: open_graph(5)).pack(pady=8)
tk.Button(root, text="Exit", width=25, height=2, bg="red", fg="white", command=root.quit).pack(pady=12)

# End of improved visualisation section
root.mainloop()

