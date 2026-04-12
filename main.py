#Implemented by Leen
# Figure 2: Histogram for Age Distribution
elif fig_num == 2:
    # Plot a histogram of the "Age" column
    df["Age"].plot(
        kind="hist",      # Specify that this is a histogram
        bins=10,          # Divide the data into 10 bins (intervals)
        ax=ax             # Draw the plot on the given axis (for GUI or subplot)
    )


    # Set the title of the graph
    ax.set_title("Age Distribution of Patients")
    
    # Label the x-axis
    ax.set_xlabel("Age")
    
    # Label the y-axis
    ax.set_ylabel("Frequency")


# Figure 3: Line graph for Age vs Heart Rate
elif fig_num == 3:
    # Sort the dataframe by Age to make the line graph look organized
    sorted_df = df.sort_values(by="Age")
    
    # Plot Age vs Heart Rate as a line graph
    ax.plot(
        sorted_df["Age"],           # X-axis values (Age)
        sorted_df["Heart_Rate"],    # Y-axis values (Heart Rate)
        marker='o',                 # Add circular markers at each data point
        linewidth=3                 # Make the line thicker for better visibility
    )
    
    # Set the title of the graph
    ax.set_title("Age vs Heart Rate")
    
    # Label the x-axis
    ax.set_xlabel("Age")
    
    # Label the y-axis
    ax.set_ylabel("Heart Rate")
    
    # Add grid lines to make the graph easier to read
    ax.grid(True)
