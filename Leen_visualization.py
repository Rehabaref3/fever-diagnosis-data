# ================================
# Import Libraries
# ================================

# pandas is used for handling and analyzing structured data (like tables)
import pandas as pd

# matplotlib.pyplot is used for creating visualizations and graphs
import matplotlib.pyplot as plt

# tkinter is used to create a simple graphical user interface (GUI)
import tkinter as tk


# ================================
# Sample Data
# ================================

# Creating a dictionary that contains sample patient data
# "Age" represents patient ages
# "Heart_Rate" represents heart rate values corresponding to each patient
data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 30, 25, 40],
    "Heart_Rate": [72, 75, 78, 80, 85, 88, 90, 77, 74, 82]
}

# Converting the dictionary into a pandas DataFrame
# DataFrame is like a table with rows and columns
df = pd.DataFrame(data)


# ================================
# Graph 1: Age Distribution (Pie Chart)
# ================================

# Function to display a pie chart showing distribution of ages
def show_age_pie():
    
    # Create a new figure window with specific size
    plt.figure(figsize=(7, 7))

    # Count how many times each age appears in the dataset
    # value_counts() groups same values and counts them
    age_counts = df["Age"].value_counts()

    # Create a pie chart
    plt.pie(
        age_counts,                # Data values (frequencies of ages)
        labels=age_counts.index,   # Labels (unique ages)
        autopct='%1.1f%%',         # Show percentage on each slice
        startangle=90,             # Rotate chart so it starts from top
        colors=plt.cm.Paired.colors  # Use a predefined color palette
    )

    # Add a title to the chart
    plt.title("Age Distribution of Patients (Pie Chart)")

    # Adjust layout to prevent overlapping elements
    plt.tight_layout()

    # Display the pie chart window
    plt.show()


# ================================
# Graph 2: Heart Rate vs Age (Bar Chart - Original)
# ================================

# Function to display a bar chart comparing age and heart rate
def show_heart_rate_bar():
    
    # Create a new figure with specific width and height
    plt.figure(figsize=(9, 5))

    # Create a bar chart
    plt.bar(
        df["Age"].astype(str),  # Convert ages to strings so they appear as categories on x-axis
        df["Heart_Rate"],       # Heights of bars (heart rate values)
        color='#e74c3c',        # Set bar color (red tone)
        alpha=0.8               # Set transparency level
    )

    # Add chart title
    plt.title("Age vs Heart Rate (Bar Chart)")

    # Label x-axis
    plt.xlabel("Age")

    # Label y-axis
    plt.ylabel("Heart Rate")

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Add horizontal grid lines to make values easier to read
    plt.grid(axis='y', linestyle='--', alpha=0.3)

    # Adjust layout to avoid overlapping labels
    plt.tight_layout()

    # Display the bar chart
    plt.show()


# ================================
# UI Window (Tkinter)
# ================================

# Create the main application window
root = tk.Tk()

# Set the window title
root.title("Health Data Visualization")

# Set window size (width x height)
root.geometry("400x250")


# Create a label (text) at the top of the window
label = tk.Label(root, text="Select Graph", font=("Arial", 14))

# Display the label with vertical spacing
label.pack(pady=20)


# Create first button to show the pie chart
btn1 = tk.Button(
    root,
    text="Age Distribution (Pie)",   # Button text
    command=show_age_pie,           # Function to run when clicked
    width=30                        # Button width
)

# Display the button with spacing
btn1.pack(pady=10)


# Create second button to show the bar chart
btn2 = tk.Button(
    root,
    text="Heart Rate (Bar Chart)",  # Button text
    command=show_heart_rate_bar,    # Function to run when clicked
    width=30
)

# Display the button
btn2.pack(pady=10)


# Start the GUI event loop
# This keeps the window open and responsive to user actions
root.mainloop()
