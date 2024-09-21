import ffn
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Get current timestamp
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Step 1: Retrieve data using ffn
data = ffn.get('nvda,msft', start='2015-01-01')

# Step 2: Save pandas dataframe as CSV with a timestamp
csv_filename = f"stock_data_{timestamp}.csv"
data.to_csv(csv_filename)

# Step 3: Generate plot
ax = data.rebase().plot(figsize=(7, 10))

# Save the plot as a PNG with a timestamp
png_filename = f"stock_plot_{timestamp}.png"
plt.savefig(png_filename)

print(f"Data saved to {csv_filename}")
print(f"Plot saved to {png_filename}")
