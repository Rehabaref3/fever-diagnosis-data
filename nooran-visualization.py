
# Graph 4: Fever Severity Levels (Horizontal Bar Chart)
# Create a new figure with custom size
plt.figure(figsize=(8,5))

# Count frequency of each fever severity level and plot as horizontal bars
df["Fever_Severity"].value_counts().plot(
    kind="barh",
    color=['#ff7675','#fdcb6e','#55efc4'])

# Add title and axis labels
plt.title("Fever Severity Levels")
plt.xlabel("Count")      # number of cases
plt.ylabel("Severity")   # severity categories

# Display the graph
plt.show()

# This graph helps us quickly understand which fever severity levels are most common in the dataset,
# which is useful for identifying patterns and checking if the data is balanced.


# Graph 5: Heart Rate by Fever Severity (Box Plot)
# Create a box plot to show heart rate distribution across severity levels
box = df.boxplot(
    column="Heart_Rate",
    by="Fever_Severity",
    patch_artist=True,
    boxprops=dict(linewidth=2),
    medianprops=dict(color='#d63031', linewidth=3),
    whiskerprops=dict(linewidth=2),
    capprops=dict(linewidth=2)
)

# Define colors for each box
colors = ['#74b9ff', '#55efc4', '#ffeaa7', '#ff7675', '#a29bfe']

# Apply colors to each box
for patch, color in zip(box.artists, colors):
    patch.set_facecolor(color)

# Add title and labels
plt.title("Heart Rate Distribution by Fever Severity", fontsize=15, fontweight="bold")
plt.suptitle("")  # remove default title
plt.xlabel("Fever Severity")
plt.ylabel("Heart Rate")

# Add grid for better readability
 plt.grid(True, linestyle='--', alpha=0.5)

# Show the plot
plt.show()

# This visualization helps compare heart rate across different severity levels,
# showing how the body response (heart rate) may increase with higher fever severity.

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

    # Create a new graph window
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
