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
