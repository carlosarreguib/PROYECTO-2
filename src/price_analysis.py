import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

# Set the style for dark background
plt.style.use('dark_background')

# Read the data
df = pd.read_csv('input/DATA_Barcelona_Fotocasa_HousingPrices_Augmented.csv')

# Remove 'Unnamed: 0' column
df = df.drop('Unnamed: 0', axis=1)

# Analyze null values
null_analysis = df.isnull().sum()
print("\nNull values in each column:")
print(null_analysis)

# Check if neighborhood has null values
if df['neighborhood'].isnull().sum() == 0:
    # Replace null values based on mode per neighborhood
    for column in df.columns:
        if df[column].isnull().any():
            df[column] = df.groupby('neighborhood')[column].transform(
                lambda x: x.fillna(x.mode().iloc[0] if not x.mode().empty else x.median())
            )

# Check price calculation consistency
price_diff = abs(df['square_meters_price'] * df['square_meters'] - df['price'])
inconsistent_prices = price_diff > 1000
print(f"\nNumber of inconsistent prices (>1000€ difference): {inconsistent_prices.sum()}")

# Remove square_meters_price column
df = df.drop('square_meters_price', axis=1)

# Detect outliers using IQR method with k=3
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 3 * IQR
upper_bound = Q3 + 3 * IQR

# Separate outliers and create clean dataframe
df_clean = df[(df['price'] >= lower_bound) & (df['price'] <= upper_bound)]
df_outliers = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]

print(f"\nNumber of outliers removed: {len(df_outliers)}")

# Analyze linear relationship between average Price and Neighborhood
avg_price_by_neighborhood = df_clean.groupby('neighborhood')['price'].mean().reset_index()
correlation = stats.pearsonr(
    pd.factorize(avg_price_by_neighborhood['neighborhood'])[0],
    avg_price_by_neighborhood['price']
)[0]

print(f"\nCorrelation between Price and Neighborhood: {correlation:.4f}")

# Create both versions of the final dataset
df_without_dummies = df_clean.copy()

# If correlation is less than 0.1, create version with dummy variables
if abs(correlation) < 0.1:
    df_with_dummies = df_clean.copy()
    neighborhood_dummies = pd.get_dummies(df_with_dummies['neighborhood'], 
                                        drop_first=True, 
                                        dtype=int)
    df_with_dummies = df_with_dummies.drop('neighborhood', axis=1)
    df_with_dummies = pd.concat([df_with_dummies, neighborhood_dummies], axis=1)
    
    # Save both versions
    df_with_dummies.to_csv('output/barcelona_housing_processed_dummies.csv', index=False)

# Save the version without dummies
df_without_dummies.to_csv('output/barcelona_housing_processed.csv', index=False)

# Create visualizations
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_clean, x='neighborhood', y='price')
plt.xticks(rotation=45, ha='right')
plt.title('Price Distribution by Neighborhood')
plt.tight_layout()
plt.savefig('output/price_distribution.png')
plt.close()

# Print final summary
print("\nProcessing completed:")
print(f"Original dataset shape: {df.shape}")
print(f"Clean dataset shape: {df_clean.shape}")
print("Files saved: barcelona_housing_processed.csv and price_distribution.png")
