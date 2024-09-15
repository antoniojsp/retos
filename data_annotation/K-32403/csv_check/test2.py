import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load the data
df = pd.read_csv('MinimumWage.csv')

# Clean the data
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df['FederalMinimumWage'] = df['FederalMinimumWage'].replace({'\$': '', ',': ''}, regex=True).astype(float)
df['MeanAnnualInflation'] = df['MeanAnnualInflation'].replace({'%': ''}, regex=True).astype(float) / 100
df['UnemploymentRateDecember'] = df['UnemploymentRateDecember'].replace({'%': ''}, regex=True).astype(float) / 100
df['GDP_AnnualGrowth'] = df['GDP_AnnualGrowth'].replace({'%': ''}, regex=True).astype(float) / 100

# Set the Year as the index
df.set_index('Year', inplace=True)

# Resample to decade frequency and calculate the mean
gdp_decade_mean = df['GDP_AnnualGrowth'].resample('10Y').mean()

# Calculate the rolling 3-decade mean
rolling_3_decade_mean = gdp_decade_mean.rolling(window=3).mean()

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(gdp_decade_mean.index, gdp_decade_mean, label='Decadal Mean GDP Growth', marker='o')
plt.plot(rolling_3_decade_mean.index, rolling_3_decade_mean, label='3-Decade Rolling Mean', color='orange')
plt.title('Decadal Mean GDP Annual Growth and 3-Decade Rolling Mean')
plt.xlabel('Year')
plt.ylabel('GDP Annual Growth')
plt.legend()
plt.grid()
plt.show()

# Decompose the Mean Annual Inflation
inflation_decomposition = sm.tsa.seasonal_decompose(df['MeanAnnualInflation'], model='additive')

# Plot the decomposition
inflation_decomposition.plot()
plt.suptitle('Time Series Decomposition of Mean Annual Inflation', fontsize=16)
plt.show()

# Cross-correlation analysis
from statsmodels.tsa.stattools import ccf

# Calculate cross-correlation
max_lag = 20
cross_corr = ccf(df['FederalMinimumWage'], df['UnemploymentRateDecember'], adjusted=False)

# Plot the cross-correlation
plt.figure(figsize=(12, 6))
plt.bar(range(max_lag), cross_corr[:max_lag], color='blue')
plt.title('Cross-Correlation between Federal Minimum Wage and Unemployment Rate')
plt.xlabel('Lag (years)')
plt.ylabel('Cross-Correlation')
plt.grid()
plt.show()