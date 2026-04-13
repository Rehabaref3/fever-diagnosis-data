# fever-diagnosis-data
# Fever Dashboard - Figure 6 & Figure 7

## What is this project?
A Python dashboard that reads a fever dataset and shows two charts for medication history.

## Files you need
- dashboard.py (the main script)
- FeverDataset1.csv (the dataset)

## How it works

### 1. Loading data
The script looks for FeverDataset1.csv in the same folder. It reads the file and keeps only the first 31 rows.

### 2. Main window
A window opens with buttons for Figure 6 and Figure 7.

### 3. Figure 6 - Bar Chart
When you click Figure 6:
- It counts how many patients took each medication
- It draws a bar chart with blue bars, light gray background, and gray grid lines behind the bars
- Percentages appear above the bars
- Patient numbers appear inside the bars in white text

### 4. Figure 7 - Donut Chart
When you click Figure 7:
- It counts the same data
- It draws a donut chart with three colored slices (purple, pink, blue)
- "Total Patients" is written in the center
- Percentages are shown outside the slices
- A legend is placed at the bottom

### 5. Navigation
Inside any chart window, you can click "Next Figure" to switch between charts, or click "Close" to go back to the main window.

## Functions explained

The script has three main functions:

- show_text(msg): This function displays messages in the text box inside the dashboard.

- build_figure(fig_num): This function creates the chart. If the number is 6, it makes the bar chart. If the number is 7, it makes the donut chart.

- open_graph_window(fig_num): This function opens a new window and shows the selected chart inside it.

## How to run
First, install pandas and matplotlib using pip. Then place the CSV file in the same folder as the script. Finally, run this command in the terminal:
python dashboard.py

## Results from the data
From the first 31 rows of the dataset, the medication results are:
- Ibuprofen was taken by 8 patients which is 47.1 percent
- Aspirin was taken by 5 patients which is 29.4 percent
- Paracetamol was taken by 4 patients which is 23.5 percent
- Total patients used in this analysis are 17
