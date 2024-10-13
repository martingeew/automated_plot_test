import ffn
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Step 1: Retrieve data using ffn
data = ffn.get("nvda,msft,googl,amzn,aapl,meta", start="2023-01-01")

# Step 2: Rebase data
data_rebase = data.rebase()


# Step 3: Generate plot
def plot_all_columns(df):
    """
    Plots all columns from the DataFrame in a single chart using Matplotlib,
    with a dark theme, no axis labels, horizontal grid lines, and no spines
    on the left, right, and top.

    Parameters:
    df (pd.DataFrame): DataFrame with float columns and DatetimeIndex as index.
    """
    # Create figure and axis
    fig, ax = plt.subplots(
        figsize=(10, 7)
    )  # Setting width to 900px and height to 600px equivalent in inches

    # Set dark background
    fig.patch.set_facecolor("#282a36")  # Background color for the figure
    ax.set_facecolor("#282a36")  # Background color for the plot area

    # Plot each column with a line
    for col in df.columns:
        ax.plot(df.index, df[col], label=col, linewidth=2)

    # Remove axis labels
    ax.set_xlabel("")  # No x-axis label
    ax.set_ylabel("")  # No y-axis label

    # Customize grid lines
    ax.grid(
        True, which="both", axis="both", color="white", alpha=0.2, linewidth=1.3
    )  # Light gray grid lines

    # Set title and legend
    ax.set_title(
        "Top tech stocks indexed to 2023-01-01=100\n",
        fontsize=20,
        color="white",
        loc="left",
    )  # Title with large font
    legend = ax.legend(
        fontsize=16,
        loc="upper left",
        frameon=True,  # Enable the frame (legend box)
        labelcolor="white",  # White legend text
        facecolor="#282a36",  # Set background color of the legend box (matching dark theme)
        framealpha=1,  # Set frame alpha to 1 for a solid fill (no transparency)
    )

    # Customize ticks
    ax.tick_params(
        axis="both", colors="white", labelsize=14
    )  # White ticks for both axes

    # Set y-axis limits (applies to both left and right since it's mirrored)
    ax.set_ylim(0, 1000)

    ax.tick_params(axis="y", which="both", labelright=True, right=True)

    # Remove the left, right, and top spines
    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_color("white")

    # Adjust layout
    plt.tight_layout()

    # Return the figure and axis
    return fig, ax


# Create the fig object
fig, ax = plot_all_columns(data_rebase)

# Step 4: Save pandas dataframe as CSV with a timestamp and Save the plot as a PNG with a timestamp in the filename
csv_filename = f"stock_data_{timestamp}.csv"
data.to_csv(csv_filename)

png_filename = f"stock_plot_{timestamp}.png"
fig.savefig(png_filename, dpi=300)  # Save with high DPI for better quality

print(f"Data saved to {csv_filename}")
print(f"Plot saved to {png_filename}")
