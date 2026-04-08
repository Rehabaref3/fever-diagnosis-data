#Implemented by Leen 
#Includes:
#Graph 2: Age distribution
#Graph 3: Age vs heart rate 

# Graph 2: Age Distribution (Histogram)
plt.figure(figsize=(9, 6))

df["Age"].plot(
    kind="hist",
    bins=10,
    color="#6c5ce7",
    edgecolor="white",
    linewidth=1.2,
    rwidth=0.9,
    alpha=0.85
)
plt.title("Age Distribution of Patients", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Frequency (Number of Patients)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.show()



# Graph 3: Age vs Heart Rate (LINE GRAPH)
sorted_df = df.sort_values(by="Age")
plt.figure(figsize=(8,5))
plt.plot(sorted_df["Age"], sorted_df["Heart_Rate"],
         marker='o',
         linewidth=3,
         color='#e74c3c')

plt.title("Age vs Heart Rate")
plt.xlabel("Age")
plt.ylabel("Heart Rate")
plt.grid(True)
plt.show()


#This part was implemented by Nooran
#includes :
#graph 4, 
#graph 5


# Graph 4: Fever Severity Levels (PIE CHART 2) -
plt.figure(figsize=(8,5))
df["Fever_Severity"].value_counts().plot(
    kind="barh",
    color=['#ff7675','#fdcb6e','#55efc4'])

plt.title("Fever Severity Levels")
plt.xlabel("Count")
plt.ylabel("Severity")
plt.show()


# Graph 5: Heart Rate by Fever Severity (Styled Box Plot)
plt.figure(figsize=(9,6))

box = df.boxplot(
    column="Heart_Rate",
    by="Fever_Severity",
    patch_artist=True,
    boxprops=dict(linewidth=2),
    medianprops=dict(color='#d63031', linewidth=3),
    whiskerprops=dict(linewidth=2),
    capprops=dict(linewidth=2) )
colors = ['#74b9ff', '#55efc4', '#ffeaa7', '#ff7675', '#a29bfe']
for patch, color in zip(box.artists, colors):
    patch.set_facecolor(color)

plt.title("Heart Rate Distribution by Fever Severity", fontsize=15, fontweight="bold")
plt.suptitle("")
plt.xlabel("Fever Severity")
plt.ylabel("Heart Rate")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

