# Import libraries
import pandas as pd  # data manipulation
import seaborn as sns  # data visualization
import matplotlib.pyplot as plt  # data visualization

# Load the Dataset
df = pd.read_csv('advanced_housing_dataset.csv')

# Display the first few rows of the dataframe
print(df.head())

# Clean Data
df.dropna(inplace=True)

# Scatter plot: GrLivArea vs SalePrice
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='GrLivArea', y='SalePrice')
plt.title('Relationship between Living Area and Sale Price')
plt.xlabel('Above Living Area (sqft)')
plt.ylabel('Sale Price ($)')
plt.show()

# Histogram of Sale Prices
plt.figure(figsize=(10, 6))
sns.histplot(df['SalePrice'], bins=20, kde=True)
plt.title('Distribution of Sale Prices')
plt.xlabel('Sale Price ($)')
plt.ylabel('Frequency')
plt.show()

# Box plot: Sale Prices by Overall Quality
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='OverallQual', y='SalePrice')
plt.title('Sale Price by Overall Quality')
plt.xlabel('Overall Quality')
plt.ylabel('Sale Price ($)')
plt.show()

# Pairplot of numerical features
sns.pairplot(df)
plt.show()

#Heatmap of Correlation Matrix
plt.figure(figsize=(12, 10))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()
