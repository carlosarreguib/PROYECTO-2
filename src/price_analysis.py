import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

# Set the style
plt.style.use('fivethirtyeight')

# Read the data
df = pd.read_csv('input/DATA_Barcelona_Fotocasa_HousingPrices_Augmented.csv')

# Remove Unnamed: 0 column
df = df.drop('Unnamed: 0', axis=1)

# Analyze null values
print("\nNull values in each column:")
print(df.isnull().sum())

# If neighborhood has no null values, fill nulls based on neighborhood mode
if df['neighborhood'].isnull().sum() == 0:
    for column in df.columns:
        if df[column].isnull().sum() > 0:
            df[column] = df.groupby('neighborhood')[column].transform(lambda x: x.fillna(x.mode().iloc[0] if not x.mode().empty else x.mean()))

# Check price calculation consistency
price_diff = abs(df['square_meters_price'] * df['square_meters'] - df['price'])
inconsistent_prices = price_diff > 500
print(f"\nNumber of inconsistent prices (>500€ difference): {inconsistent_prices.sum()}")

# Remove square_meters_price column
df = df.drop('square_meters_price', axis=1)

# Detect outliers in price using IQR method
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\nOutliers in price:")
print(f"Number of outliers: {((df['price'] < lower_bound) | (df['price'] > upper_bound)).sum()}")

# Create clean dataframe without outliers
df_clean = df[~((df['price'] < lower_bound) | (df['price'] > upper_bound))]

# Analyze linear relationship between average price and neighborhood
avg_price_by_neighborhood = df_clean.groupby('neighborhood')['price'].mean().reset_index()
neighborhoods = avg_price_by_neighborhood['neighborhood'].values
prices = avg_price_by_neighborhood['price'].values
correlation = stats.pearsonr(range(len(neighborhoods)), prices)[0]

print(f"\nCorrelation coefficient between neighborhood and average price: {correlation:.4f}")

# If correlation is less than 0.1, create dummy variables
if abs(correlation) < 0.1:
    print("\nCreating dummy variables for neighborhood...")
    df_clean = pd.get_dummies(df_clean, columns=['neighborhood'], drop_first=True)

# Save the final dataframe
output_path = 'output/barcelona_housing_processed.csv'
df_clean.to_csv(output_path, index=False)
print(f"\nProcessed data saved to: {output_path}")

# Create visualizations
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='price')
plt.title('Price Distribution with Outliers')
plt.savefig('output/price_distribution.png')
plt.close()

plt.figure(figsize=(15, 8))
sns.barplot(data=avg_price_by_neighborhood, x='neighborhood', y='price')
plt.xticks(rotation=45, ha='right')
plt.title('Average Price by Neighborhood')
plt.tight_layout()
plt.savefig('output/avg_price_by_neighborhood.png')
plt.close()
