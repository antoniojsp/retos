import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import ccf

# Load the CSV file
df = pd.read_csv("MinimumWage.csv")

# Data Cleaning and Preprocessing
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df = df.set_index('Year')

df['FederalMinimumWage'] = df['FederalMinimumWage'].astype(str).str.replace(r'[$,]', '', regex=True).astype(float)
for col in ['MeanAnnualInflation', 'UnemploymentRateDecember', 'GDP_AnnualGrowth']:
    df[col] = df[col].astype(str).str.replace('%', '', regex=False).astype(float) / 100


# 1. Resample to Decade and Calculate Rolling Mean of GDP Growth
decade_df = df['GDP_AnnualGrowth'].resample('10AS').mean()  # '10AS' for decade start frequency
rolling_mean = decade_df.rolling(window=3, center=True).mean()

plt.figure(figsize=(10, 4))
plt.plot(decade_df, label='Decade GDP Growth')
plt.plot(rolling_mean, label='3-Decade Rolling Mean', color='red')
plt.title('GDP Growth by Decade and 3-Decade Rolling Mean')
plt.legend()
plt.show()


# 2. Time Series Decomposition of Mean Annual Inflation
decomposition = seasonal_decompose(df['MeanAnnualInflation'], model='additive', period=10) # Using a period of 10 years as a reasonable assumption for economic cycles

plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(df['MeanAnnualInflation'], label='Original')
plt.legend(loc='upper left')
plt.subplot(412)
plt.plot(decomposition.trend, label='Trend')
plt.legend(loc='upper left')
plt.subplot(413)
plt.plot(decomposition.seasonal, label='Seasonal')
plt.legend(loc='upper left')
plt.subplot(414)
plt.plot(decomposition.resid, label='Residual')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()



# 3. Cross-Correlation Analysis of Federal Minimum Wage and Unemployment
# Interpolate missing values for cross-correlation analysis
df['FederalMinimumWage'] = df['FederalMinimumWage'].interpolate(method='linear')
df['UnemploymentRateDecember'] = df['UnemploymentRateDecember'].interpolate(method='linear')

cross_corr = ccf(df['FederalMinimumWage'], df['UnemploymentRateDecember'], adjusted=False)
lags = list(range(-len(cross_corr) // 2 + 1, len(cross_corr) // 2))

plt.figure(figsize=(10, 4))
plt.stem(lags, cross_corr)
plt.title('Cross-Correlation between Federal Minimum Wage and Unemployment')
plt.xlabel('Lag')
plt.ylabel('Cross-Correlation')
plt.show()