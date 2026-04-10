import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("enhanced_fever_medicine_recommendation 2.csv")
plt.style.use('ggplot')

plt.figure(figsize=(7,7))
med_counts = df["Previous_Medication"].value_counts()
total = sum(med_counts)

def autopct_with_numbers(pct):
    count = int(round(pct * total / 100.0))
    return f'{pct:.1f}% ({count})'

med_counts.plot(kind="pie", autopct=autopct_with_numbers, startangle=90)
plt.title("Previous Medication Distribution")
plt.ylabel("")
plt.show()

