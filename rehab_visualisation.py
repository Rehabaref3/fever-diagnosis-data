# Import required libraries
import pandas as pd                # For data manipulation and analysis
import matplotlib.pyplot as plt    # For creating visualizations

# Load the dataset from CSV file
df = pd.read_csv("FeverDataset1.csv")
df = df.head(31)                   # Take only the first 31 rows
plt.style.use('ggplot')

med_counts = df["Previous_Medication"].value_counts()

# ========== BAR CHART ==========
plt.figure(figsize=(10,6))                              
med_counts.plot(kind="bar", color="steelblue", edgecolor="black")
plt.title("Previous Medication Distribution - Bar Chart", fontsize=14)
plt.xlabel("Medication Name", fontsize=12)
plt.ylabel("Number of Patients", fontsize=12)
plt.xticks(rotation=0, ha="center")                     
plt.grid(axis="y", linestyle="--", alpha=0.7)           

total = sum(med_counts)  
for i, v in enumerate(med_counts):
    pct = (v / total) * 100
    plt.text(i, v + 0.1, f'{pct:.1f}%', ha="center", fontsize=10, fontweight="bold")

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
