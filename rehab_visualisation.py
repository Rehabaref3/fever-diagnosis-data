# Import required libraries
import pandas as pd                # For data manipulation and analysis
import matplotlib.pyplot as plt    # For creating visualizations

# Load the dataset from CSV file
df = pd.read_csv("FeverDataset1.csv")
df = df.head(31)                   # Take only the first 31 rows
plt.style.use('ggplot')            # Apply a professional plot style

# ==========  PIE CHART ==========
# Creat a new figure with specific size 
plt.figure(figsize=(7,7))          
med_counts = df["Previous_Medication"].value_counts()    # Count how many patients took each medication
total = sum(med_counts)                                  # Calculate total number of patients

# Create a custom function to display percentage + actual count
def autopct_with_numbers(pct):
    count = int(round(pct * total / 100.0))              # Calculate actual number
    return f'{pct:.1f}% ({count})'                       # Display like: "33.6% (256)"

# Create the Pie Chart 
med_counts.plot(kind="pie", autopct=autopct_with_numbers, startangle=90) 
plt.title("Previous Medication Distribution")            # Add Title
plt.ylabel("")                                           # Remove the y-axis label (not needed for pie chart)
plt.show()                                               # Display the chart


# ================================================
# IMPROVEMENTS MADE COMPARED TO ORIGINAL CODE:
# 1. Added actual patient numbers next to percentages
# 2. Used custom function autopct_with_numbers for better readability
# 3. Calculated total patients for accurate counting
# ================================================

# ========== BAR CHART ==========
plt.figure(figsize=(10,6))                              
med_counts.plot(kind="bar", color="steelblue", edgecolor="black")
plt.title("Previous Medication Distribution - Bar Chart", fontsize=14)
plt.xlabel("Medication Name", fontsize=12)
plt.ylabel("Number of Patients", fontsize=12)
plt.xticks(rotation=45, ha="right")                     
plt.grid(axis="y", linestyle="--", alpha=0.7)           

for i, v in enumerate(med_counts):
    plt.text(i, v + 0.3, str(v), ha="center", fontsize=10, fontweight="bold")

plt.tight_layout()
plt.show()

# Print the results
print("\n" + "="*50)
print("RESULTS FOR FIRST 31 PATIENTS")
print("="*50)
print("\nPrevious Medication Counts:")
print(med_counts)
print(f"\nTotal patients: {total}")
print("\n" + "="*50)
