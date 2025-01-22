import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')
import seaborn as sns

# Read the data
df = pd.read_csv('input/DATA_Barcelona_Fotocasa_HousingPrices_Augmented.csv')

#Shape of the dataset
print("\n1. Shape of the dataset:")
print(df.shape)

# Remove Unnamed: 0 column
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)
    print("\n2. Unnamed: 0 column has been removed")

# Check for null values
null_values = df.isnull().sum()
print("\n3. Null values in the dataset:")
print(null_values[null_values > 0])

# Check price calculation
df['calculated_price'] = df.square_meters_price * df.square_meters
price_diff = abs(df.price - df.calculated_price)
inconsistent_prices = df[price_diff > 200]  # Being tolerable with the price difference

print("\n4. Price calculation check:")
print(f"Number of inconsistent prices: {len(inconsistent_prices)}")
if len(inconsistent_prices) > 0:
    print("\nSample of inconsistent prices:")
    print(inconsistent_prices[['price', 'square_meters_price', 'square_meters', 'calculated_price']].head(10))

# Detect price outliers using IQR method
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df.price < lower_bound) | (df.price > upper_bound)]

print("\n5. Price outliers analysis:")
print(f"Number of outliers detected: {len(outliers)}")
print(f"Percentage of outliers: {(len(outliers)/len(df))*100:.2f}%")
print(f"Price range for non-outliers: {lower_bound:,.2f} - {upper_bound:,.2f}")

# Create a box plot for price
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['price'])
plt.title('Box Plot of Housing Prices')
plt.xlabel('Price')
plt.savefig('output/price_boxplot.png')
plt.close()

# Display summary statistics of outliers
if len(outliers) > 0:
    print("\nSummary statistics of outlier properties:")
    print(outliers[['price', 'square_meters', 'square_meters_price']].describe())
