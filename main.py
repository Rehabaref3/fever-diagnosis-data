#Implemented by Leen
# Figure 2: Histogram for Age Distribution
    elif fig_num == 2:
        df["Age"].plot(
            kind="hist",
            bins=10,
            ax=ax
        )
        ax.set_title("Age Distribution of Patients")
        ax.set_xlabel("Age")
        ax.set_ylabel("Frequency")

    # Figure 3: Line graph for Age vs Heart Rate
    elif fig_num == 3:
        sorted_df = df.sort_values(by="Age")
        ax.plot(
            sorted_df["Age"],
            sorted_df["Heart_Rate"],
            marker='o',
            linewidth=3
        )
        ax.set_title("Age vs Heart Rate")
        ax.set_xlabel("Age")
        ax.set_ylabel("Heart Rate")
        ax.grid(True)
