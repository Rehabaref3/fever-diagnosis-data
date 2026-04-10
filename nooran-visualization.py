
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
