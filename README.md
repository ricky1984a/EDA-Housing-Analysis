# Exploratory Data Analysis (EDA) Using Python

The script demonstrates an exploratory data analysis (EDA) process using Python with the following libraries:
- **Pandas** for data manipulation
- **Seaborn** and **Matplotlib** for data visualization

Below is a detailed breakdown of the analysis:

---

## 1. Importing Libraries
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```
- `pandas` is used for data handling and cleaning.
- `seaborn` and `matplotlib.pyplot` are employed to generate visually appealing plots.

---

## 2. Loading the Dataset
```python
df = pd.read_csv('advanced_housing_dataset.csv')
print(df.head())
```
- The dataset is loaded into a Pandas DataFrame from a CSV file named `advanced_housing_dataset.csv`.
- The first few rows are displayed to preview the structure of the dataset.

---

## 3. Cleaning the Data
```python
df.dropna(inplace=True)
```
- Missing values are dropped to ensure a clean dataset for analysis.
- This step reduces the risk of errors during visualization and improves data integrity.

---

## 4. Visualization and Analysis

### 4.1 Scatter Plot: Living Area vs. Sale Price
```python
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='GrLivArea', y='SalePrice')
plt.title('Relationship between Living Area and Sale Price')
plt.xlabel('Above Living Area (sqft)')
plt.ylabel('Sale Price ($)')
plt.show()
```
- **Objective**: To analyze the relationship between the above-grade living area (`GrLivArea`) and sale price (`SalePrice`).
- The scatter plot reveals patterns such as clustering, outliers, and potential linear relationships.

---

### 4.2 Histogram of Sale Prices
```python
plt.figure(figsize=(10, 6))
sns.histplot(df['SalePrice'], bins=20, kde=True)
plt.title('Distribution of Sale Prices')
plt.xlabel('Sale Price ($)')
plt.ylabel('Frequency')
plt.show()
```
- **Objective**: To examine the distribution of house sale prices.
- The histogram with a kernel density estimate (KDE) overlay provides insights into the central tendency, spread, and skewness of `SalePrice`.

---

### 4.3 Box Plot: Sale Prices by Overall Quality
```python
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='OverallQual', y='SalePrice')
plt.title('Sale Price by Overall Quality')
plt.xlabel('Overall Quality')
plt.ylabel('Sale Price ($)')
plt.show()
```
- **Objective**: To compare sale prices across different levels of overall quality (`OverallQual`).
- The box plot highlights the median sale price, interquartile range, and outliers for each quality level.

---

### 4.4 Pairplot of Numerical Features
```python
sns.pairplot(df)
plt.show()
```
- **Objective**: To explore relationships between multiple numerical features in the dataset.
- Pairplots facilitate quick identification of trends and interactions between variables.

---

### 4.5 Heatmap of Correlation Matrix
```python
plt.figure(figsize=(12, 10))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()
```
- **Objective**: To examine the correlation between numerical variables in the dataset.
- The heatmap helps identify highly correlated features, which may be useful for feature selection in predictive modeling.

---

## Key Takeaways
- The scatter plot indicates whether larger living areas correlate with higher sale prices.
- The histogram reveals the distribution of sale prices, showing whether the data is skewed or normally distributed.
- The box plot demonstrates how quality affects pricing, useful for understanding price variation by build quality.
- The pairplot gives a comprehensive view of relationships between all numerical variables, aiding in identifying trends and anomalies.
- The correlation heatmap provides a detailed understanding of how features are interrelated, which is crucial for advanced modeling techniques.

This EDA provides valuable insights for further analysis or predictive modeling in the housing market.
