import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# Set the style for plots
plt.style.use('fivethirtyeight')

# Read the data
df = pd.read_csv('input/DATA_Barcelona_Fotocasa_HousingPrices_Augmented.csv')
print("\n")
print(df.dtypes)

# Remove Unnamed: 0 column
df = df.drop('Unnamed: 0', axis=1)

# Check null values
print("\nNull values in each column:")
print(df.isnull().sum())

# If neighborhood has no null values, fill nulls based on mode per neighborhood
if df['neighborhood'].isnull().sum() == 0:
    for column in df.columns:
        if column != 'neighborhood' and df[column].isnull().any():
            df[column] = df.groupby('neighborhood')[column].transform(lambda x: x.fillna(x.mode().iloc[0] if not x.mode().empty else x.mean()))

# Convert rooms, bathroom and square_meters to int
df['rooms'] = df['rooms'].round().astype(int)
df['bathroom'] = df['bathroom'].round().astype(int)
df['square_meters'] = df['square_meters'].round().astype(int)

# Check price consistency
price_diff = abs(df['square_meters_price'] * df['square_meters'] - df['price'])
inconsistent_prices = price_diff > 1000
print("\nNumber of inconsistent prices:", inconsistent_prices.sum())

# Remove square_meters_price column
df = df.drop('square_meters_price', axis=1)

# Detect outliers using IQR method
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
k = 2.5
lower_bound = Q1 - k * IQR
upper_bound = Q3 + k * IQR

# Remove outliers
df_no_outliers = df[(df['price'] >= lower_bound) & (df['price'] <= upper_bound)]
print(f"\nRemoved {len(df) - len(df_no_outliers)} outliers")

# Create boxplot
plt.figure(figsize=(15, 8))
sns.boxplot(data=df_no_outliers, x='neighborhood', y='price')
plt.xticks(rotation=45, ha='right')
plt.title('Price Distribution by Neighborhood')
plt.tight_layout()
plt.savefig('output/price_neighborhood_boxplot.png')
plt.close()

# Calculate correlation using one-way ANOVA
neighborhoods = df_no_outliers['neighborhood'].unique()
price_groups = [df_no_outliers[df_no_outliers['neighborhood'] == n]['price'] for n in neighborhoods]
f_statistic, p_value = stats.f_oneway(*price_groups)
correlation = np.sqrt(f_statistic / (f_statistic + len(df_no_outliers) - len(neighborhoods)))
print(f"\nCorrelation strength (based on ANOVA): {correlation:.4f}")

# If correlation is less than 0.25, create dummy variables
if correlation < 0.25:
    df_dummy = pd.get_dummies(df_no_outliers, columns=['neighborhood'], drop_first=True, dtype=int)
    # Save both versions
    df_dummy.to_csv('output/housing_prices_dummy.csv', index=False)
    df_no_outliers.to_csv('output/housing_prices_processed.csv', index=False)
else:
    df_no_outliers.to_csv('output/housing_prices_processed.csv', index=False)
    print("\nCorrelation is >= 0.25, dummy variables were not created")
