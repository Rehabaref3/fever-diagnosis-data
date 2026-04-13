import os #Used to handle file paths
import pandas as pd # Used tp read and process the dataset
import tkinter as tk   # GUI library for creating the dashboard window
from matplotlib.figure import Figure # Used to create plots
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Embeds plots into Tkinter

# Improved visualisations using the same dataset variables
# Create main application window

root = tk.Tk()
root.title("Improved Visualisation Dashboard")
root.geometry("560x420")

title = tk.Label(root, text="Improved Visualisation Dashboard", font=("Arial", 16, "bold"))
title.pack(pady=12)

text_box = tk.Text(root, height=7, width=60)
text_box.pack(pady=10)
def show_text(msg):
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, msg)
    print(msg)
    print("-" * 50)
    df = None
    try:
    current_folder = os.path.dirname(__file__)
    file_path = os.path.join(current_folder, "FeverDataset1.csv")
    df = pd.read_csv(file_path)
    df = df.head(31)
    show_text(f"File read successfully.\nRows loaded: {len(df)}")
except Exception as e:
    show_text(f"Error reading file:\n{e}")
def build_figure(fig_num):
    fig = Figure(figsize=(7, 5), dpi=100)
    ax = fig.add_subplot(111)

   # Figure 4: Pareto Chart for Fever Severity
    if fig_num == 4:
        severity_counts = df["Fever_Severity"].value_counts().sort_values(ascending=False)
        cumulative_percent = severity_counts.cumsum() / severity_counts.sum() * 100
ax.bar(severity_counts.index, severity_counts.values)

        ax.set_title("Pareto Analysis of Fever Severity Levels", fontsize=14, fontweight="bold")
        ax.set_xlabel("Fever Severity")
        ax.set_ylabel("Frequency")
        ax.grid(axis="y", linestyle="--", alpha=0.4)

for i, value in enumerate(severity_counts.values):
            ax.text(i, value + 0.1, str(value), ha="center", fontsize=9)

  ax2 = ax.twinx()
        ax2.plot(severity_counts.index, cumulative_percent.values, marker="o", linewidth=2)
        ax2.set_ylabel("Cumulative Percentage (%)")
        ax2.set_ylim(0, 110)

        for i, cp in enumerate(cumulative_percent.values):
            ax2.text(i, cp + 2, f"{cp:.1f}%", ha="center", fontsize=8)

  # Figure 5: Box Plot with Raw Data Points
    elif fig_num == 5:
        severity_order = sorted(df["Fever_Severity"].dropna().unique())
 grouped_data = [
            df[df["Fever_Severity"] == level]["Heart_Rate"].dropna()
            for level in severity_order
        ]
        colors = ["skyblue", "lightgreen", "salmon", "plum", "khaki"]

        bp = ax.boxplot(
            grouped_data,
            patch_artist=True,
            labels=severity_order,
            widths=0.5
        )
        for box, color in zip(bp["boxes"], colors):
            box.set_facecolor(color)
            box.set_alpha(0.35)
            box.set_edgecolor("black")

 for i, (group, color) in enumerate(zip(grouped_data, colors), start=1):
            jittered_x = [i + ((j - len(group)/2) * 0.02) for j in range(len(group))]
            ax.scatter(jittered_x, group, alpha=0.8, s=25, color=color, edgecolors="black", linewidths=0.3)

            mean_value = group.mean()
            ax.text(i + 0.05, mean_value, f"{mean_value:.1f}", fontsize=8)
ax.set_title("Heart Rate Distribution by Fever Severity")
        ax.set_xlabel("Fever Severity")
        ax.set_ylabel("Heart Rate")
        ax.grid(axis="y", linestyle="--", alpha=0.4)

    return fig
def open_graph(fig_num):
    if df is None:
        show_text("Dataset not loaded.")
        return
def open_graph(fig_num):
    if df is None:
        show_text("Dataset not loaded.")
        return
 if fig_num == 4:
        show_text("Figure 4 opened successfully.\nImproved Cleveland dot plot was generated.")
    elif fig_num == 5:
        show_text("Figure 5 opened successfully.\nImproved box plot with raw data points was generated.")
        = tk.Toplevel(root)
    win.title(f"Figure {fig_num}")
    win.geometry("800x650")

    fig = build_figure(fig_num)
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)

    fig = build_figure(fig_num)
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)


    if fig_num == 4:
        tk.Button(btn_frame, text="Next Figure", width=15,
                  command=lambda: [win.destroy(), open_graph(5)]).pack(side="left", padx=10)
tk.Button(root, text="Open Figure 4", width=25, height=2, command=lambda: open_graph(4)).pack(pady=8)
tk.Button(root, text="Open Figure 5", width=25, height=2, command=lambda: open_graph(5)).pack(pady=8)
tk.Button(root, text="Exit", width=25, height=2, bg="red", fg="white", command=root.quit).pack(pady=12)

# End of improved visualisation section
root.mainloop()

