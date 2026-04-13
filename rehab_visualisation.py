import os
import pandas as pd
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Create the main application window
root = tk.Tk()
root.title("Fever Dataset Dashboard")
root.geometry("560x620")

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

    # Implemented by Leen
    # Includes:
    # Graph 2: Age distribution
    # Graph 3: Age vs heart rate

    # Graph 2: Age Distribution (Histogram)
    elif fig_num == 2:
        df["Age"].plot(
            kind="hist",
            bins=10,
            color="#6c5ce7",
            edgecolor="white",
            linewidth=1.2,
            rwidth=0.9,
            alpha=0.85,
            ax=ax
        )
        ax.set_title("Age Distribution of Patients", fontsize=14, fontweight="bold", pad=15)
        ax.set_xlabel("Age", fontsize=12)
        ax.set_ylabel("Frequency (Number of Patients)", fontsize=12)
        ax.grid(axis="y", linestyle="--", alpha=0.3)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    # Graph 3: Age vs Heart Rate (LINE GRAPH)
    elif fig_num == 3:
        sorted_df = df.sort_values(by="Age")
        ax.plot(
            sorted_df["Age"],
            sorted_df["Heart_Rate"],
            marker="o",
            linewidth=3,
            color="#e74c3c"
        )
        ax.set_title("Age vs Heart Rate")
        ax.set_xlabel("Age")
        ax.set_ylabel("Heart Rate")
        ax.grid(True)

    # This part was implemented by Nooran
    # includes:
    # graph 4,
    # graph 5

    # Figure 4: Horizontal bar chart for Fever Severity
    # This graph shows the frequency of each fever severity category.
    elif fig_num == 4:
        df["Fever_Severity"].value_counts().plot(
            kind="barh",
            ax=ax
        )
        ax.set_title("Fever Severity Levels")
        ax.set_xlabel("Count")
        ax.set_ylabel("Severity")

    # Figure 5: Box plot for Heart Rate by Fever Severity
    # This graph compares heart rate distribution across fever severity levels.
    elif fig_num == 5:
        df.boxplot(
            column="Heart_Rate",
            by="Fever_Severity",
            ax=ax,
            patch_artist=True,
            boxprops=dict(linewidth=2),
            medianprops=dict(color="#d63031", linewidth=3),
            whiskerprops=dict(linewidth=2),
            capprops=dict(linewidth=2)
        )

        colors = ["#74b9ff", "#55efc4", "#ffeaa7", "#ff7675", "#a29bfe"]
        for patch, color in zip(ax.patches, colors):
            patch.set_facecolor(color)

        ax.set_title("Heart Rate Distribution by Fever Severity")
        fig.suptitle("")
        ax.set_xlabel("Fever Severity")
        ax.set_ylabel("Heart Rate")
        ax.grid(True)

    # rehab_visualisation_individual

    # Figure 6: Bar chart for Previous Medication 
    elif fig_num == 6:
        # Calculate value counts for Previous Medication
        med_counts = df["Previous_Medication"].value_counts()
        
        # Set light gray background color 
        ax.set_facecolor('#f5f5f5')
        fig.patch.set_facecolor('#f5f5f5')
        
        # Draw bars first
        med_counts.plot(kind="bar", color="steelblue", edgecolor="black", linewidth=1.5, ax=ax, width=0.6)
        
        # Force grid to be behind bars
        ax.set_axisbelow(True)
        
        # Draw gray grid lines behind bars 
        ax.grid(axis="y", linestyle="--", alpha=0.8, color='gray')
        ax.grid(axis="x", linestyle="none")  # No vertical grid lines
        
        # Remove top and right spines for cleaner look
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('gray')
        ax.spines['bottom'].set_color('gray')
        
        # Set chart title and labels
        ax.set_title("Previous Medication Distribution - Bar Chart", fontsize=14, fontweight='bold')
        ax.set_xlabel("Medication Name", fontsize=12)
        ax.set_ylabel("Number of Patients", fontsize=12)
        
        # Rotate x-axis labels to horizontal
        ax.set_xticklabels(med_counts.index, rotation=0, ha="center")
        
        # Set y-axis limits to give space for percentage labels
        max_val = max(med_counts)
        ax.set_ylim(0, max_val + 2)
        
        # Add percentage labels on top of each bar
        total = sum(med_counts)
        for i, v in enumerate(med_counts):
            pct = (v / total) * 100
            ax.text(i, v + 0.3, f'{pct:.1f}%', ha="center", fontsize=11, fontweight='bold')
        
        # Add value labels inside bars at the bottom
        for i, v in enumerate(med_counts):
            ax.text(i, v - 0.5, str(v), ha="center", fontsize=10, color='white', fontweight='bold')

    # Figure 7: Donut Chart for Previous Medication Distribution 
    elif fig_num == 7:
        # Calculate the frequency of each medication type
        med_counts = df["Previous_Medication"].value_counts()
        
        # Define custom colors for each medication category
        colors = ["#a063b8", "#cc4a78", "#5fa8df"]  # Purple, Pink, Blue
        
        # Create the donut chart
        # labels=None removes medication names from the chart
        wedges, texts, autotexts = ax.pie(
            med_counts.values,
            labels=None,  # No medication names on the chart
            autopct=lambda pct: f'{pct:.1f}%',
            colors=colors,
            startangle=90,
            wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2),
            textprops={'fontsize': 11, 'fontweight': 'bold', 'color': 'black'},
            pctdistance=1.2  # Percentages outside the donut
        )
        
        # Calculate total number of patients
        total_patients = sum(med_counts.values)
        
        # Add "Total Patients" text in the center
        ax.text(
            0, 0,
            f'Total Patients\n{total_patients}',
            ha='center',
            va='center',
            fontsize=12,
            fontweight='bold'
        )
        
        # Set the title
        ax.set_title(
            "Previous Medication Distribution - Donut Chart", 
            fontsize=14, 
            fontweight='bold'
        )
        
        # Make the chart perfectly circular
        ax.axis('equal')
        
        # LEGEND PLACEMENT - Raised to touch the donut
        ax.legend(
            wedges,
            [f'{label} ({count} patients)' for label, count in zip(med_counts.index, med_counts.values)],
            title="Medication Types",
            loc="upper center",
            bbox_to_anchor=(0.5, -0.00),  # Raised higher to touch the donut
            frameon=True,
            facecolor='white',
            edgecolor='black',
            fontsize=10,
            ncol=3
        )

    return fig

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
    elif fig_num == 6:
        show_text("Figure 6 opened successfully.\nBar chart for Previous Medication Distribution was generated.")
        # Print results to console
        med_counts = df["Previous_Medication"].value_counts()
        total = sum(med_counts)
        print("\n" + "="*50)
        print("RESULTS FOR BAR CHART")
        print("="*50)
        print("\nPrevious Medication Counts:")
        print(med_counts)
        print(f"\nTotal patients: {total}")
        print("\n" + "="*50)
    elif fig_num == 7:
        show_text("Figure 7 opened successfully.\nDonut chart for Previous Medication Distribution was generated.")
        # Print results to console
        med_counts = df["Previous_Medication"].value_counts()
        total = sum(med_counts)
        print("\n" + "="*50)
        print("RESULTS FOR DONUT CHART")
        print("="*50)
        print("\nPrevious Medication Counts:")
        print(med_counts)
        print(f"\nTotal patients: {total}")
        print("\n" + "="*50)

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
    if fig_num < 7:
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
tk.Button(root, text="Figure 1 (Pie Chart - Medication)", command=lambda: open_graph_window(1), width=30).pack(pady=5)
tk.Button(root, text="Figure 2 (Histogram - Age)", command=lambda: open_graph_window(2), width=30).pack(pady=5)
tk.Button(root, text="Figure 3 (Line - Age vs Heart Rate)", command=lambda: open_graph_window(3), width=30).pack(pady=5)
tk.Button(root, text="Figure 4 (Horizontal Bar - Fever Severity)", command=lambda: open_graph_window(4), width=30).pack(pady=5)
tk.Button(root, text="Figure 5 (Box Plot - Heart Rate by Severity)", command=lambda: open_graph_window(5), width=30).pack(pady=5)
tk.Button(root, text="Figure 6 (Bar Chart - Medication)", command=lambda: open_graph_window(6), width=30).pack(pady=5)
tk.Button(root, text="Figure 7 (Donut Chart - Medication)", command=lambda: open_graph_window(7), width=30).pack(pady=5)

# Add an Exit button to close the dashboard
tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", width=30).pack(pady=15)

# Run the application
root.mainloop()
print("RESULTS FOR FIRST 31 PATIENTS")
print("="*50)
print("\nPrevious Medication Counts:")
print(med_counts)
print(f"\nTotal patients: {total}")
print("\n" + "="*50)
