import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates


def plot_award_trends(df):
    """Visualizes the cumulative count of awards over time for different categories and award types.

    Generates a separate plot for each category, showing the cumulative sum of awards for each award type
    as a scatter plot with different colors and z-orders. Plots are saved as PNG files.

    Args:
      df: A Pandas DataFrame with columns 'category', 'award', 'time' (Unix time in UTC+8), and 'num'.

    Returns:
      None.
    """
    # Convert time to UTC and then to datetime
    df['datetime'] = pd.to_datetime(df['time'] + 28800, unit='s')

    # Sort the dataframe by datetime
    df = df.sort_values('datetime')

    # Define colors and z-orders for award types
    colors = {"Gold": "gold", "Silver": "silver", "Bronze": "brown"}
    zorders = {"Gold": 3, "Silver": 2, "Bronze": 1}

    # Group by category
    for category, group in df.groupby('category'):
        plt.figure(figsize=(10, 6))

        # Group by award type within each category
        for award, award_group in group.groupby('award'):
            # Calculate cumulative sum
            cumsum = award_group.groupby('datetime')['num'].sum().cumsum()

            # Plot scatter
            plt.scatter(cumsum.index, cumsum.values,
                        label=award,
                        color=colors.get(award, 'gray'),
                        zorder=zorders.get(award, 0),
                        s=30)  # s parameter sets the size of scatter points

        plt.title(category)
        plt.xlabel('Time')
        plt.ylabel('Cumulative Count of Awards')

        # Format x-axis to show time as HH:MM
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
        plt.gcf().autofmt_xdate()  # Rotate and align the tick labels

        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)

        # Save the plot
        plt.savefig(f"{category}.png", dpi=300, bbox_inches='tight')
        plt.close()

# Example usage:
data = pd.DataFrame({
    'category': ['Sports', 'Sports', 'Arts', 'Arts', 'Sports', 'Arts'],
    'award': ['Gold', 'Silver', 'Gold', 'Bronze', 'Bronze', 'Silver'],
    'time': [1678876800, 1678878600, 1678880400, 1678882200, 1678884000, 1678885800],
    'num': [2, 1, 3, 2, 1, 2]
})
plot_award_trends(data)