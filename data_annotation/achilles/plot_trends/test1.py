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
    import matplotlib.pyplot as plt
    from datetime import datetime

    zorders = {"Gold": 3, "Silver": 2, "Bronze": 1}

    for category in df['category'].unique():
        category_df = df[df['category'] == category]

        plt.figure()
        plt.title(category)
        plt.xlabel('Time (HH:MM)')
        plt.ylabel('Cumulative Award Count')

        for award in category_df['award'].unique():
            award_df = category_df[category_df['award'] == award]
            award_df['time'] = award_df['time'].apply(lambda x: datetime.utcfromtimestamp(x + 28800).strftime("%H:%M"))
            award_df['cumulative_sum'] = award_df['num'].cumsum()

            plt.scatter(award_df['time'], award_df['cumulative_sum'], label=award, zorder=zorders[award])

        plt.legend()
        plt.savefig(f'{category}.png', dpi=300)
        plt.close()

data = pd.DataFrame({
    'category': ['Sports', 'Sports', 'Arts', 'Arts', 'Sports', 'Arts'],
    'award': ['Gold', 'Silver', 'Gold', 'Bronze', 'Bronze', 'Silver'],
    'time': [1678876800, 1678878600, 1678880400, 1678882200, 1678884000, 1678885800],
    'num': [2, 1, 3, 2, 1, 2]
})
plot_award_trends(data)