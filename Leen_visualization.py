# Implemented by Leen

# This section includes:
# Graph 2: Age Distribution (Histogram)
# Graph 3: Relationship between Age and Heart Rate (Line Graph)


# -------------------------------
# Graph 2: Age Distribution
# -------------------------------

# Create a figure with a specified size for better visualization
plt.figure(figsize=(9, 6))

# Plot a histogram to show how patient ages are distributed
df["Age"].plot(
    kind="hist",          # Histogram type
    bins=10,              # Number of intervals (bins)
    color="#6c5ce7",      # Bar color
    edgecolor="white",    # Border color between bars
    linewidth=1.2,        # Thickness of bar edges
    rwidth=0.9,           # Width of bars (slight spacing between them)
    alpha=0.85            # Transparency level
)

# Add title and labels for clarity
plt.title("Age Distribution of Patients", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency (Number of Patients)", fontsize=12)

# Add a horizontal grid to improve readability of frequencies
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Remove unnecessary borders for a cleaner, modern look
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the histogram
plt.show()



# -------------------------------
# Graph 3: Age vs Heart Rate
# -------------------------------

# Sort the dataset by Age to ensure a smooth and logical line progression
sorted_df = df.sort_values(by="Age")

# Create a new figure for the line graph
plt.figure(figsize=(8,5))

# Plot Age against Heart Rate using a line graph
plt.plot(
    sorted_df["Age"], 
    sorted_df["Heart_Rate"],
    marker='o',        # Add markers to highlight each data point
    linewidth=3,       # Thickness of the line
    color='#e74c3c'    # Line color
)

# Add title and axis labels
plt.title("Age vs Heart Rate")
plt.xlabel("Age")
plt.ylabel("Heart Rate")

# Add grid lines for better readability
plt.grid(True)

# Display the line graph
plt.show()
