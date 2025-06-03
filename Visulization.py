
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load dataset
df = pd.read_csv('zomato.csv', encoding='latin-1')

# Clean dataset
df_clean = df.copy()
df_clean = df_clean.dropna(subset=['name', 'location', 'rate', 'approx_cost(for two people)', 'cuisines'])

df_clean['rate'] = df_clean['rate'].apply(lambda x: str(x).split('/')[0].strip() if isinstance(x, str) else np.nan)
df_clean['rate'] = pd.to_numeric(df_clean['rate'], errors='coerce')

df_clean['approx_cost(for two people)'] = df_clean['approx_cost(for two people)'].str.replace(',', '')
df_clean['approx_cost(for two people)'] = pd.to_numeric(df_clean['approx_cost(for two people)'], errors='coerce')

df_clean = df_clean.dropna(subset=['rate', 'approx_cost(for two people)'])
df_clean['cuisines'] = df_clean['cuisines'].str.strip()

# Analysis
cuisine_series = df_clean['cuisines'].str.split(', ')
cuisine_flat = [c for sublist in cuisine_series for c in sublist]
top_cuisines = pd.Series(Counter(cuisine_flat)).sort_values(ascending=False).head(10)

top_locations = df_clean['location'].value_counts().head(10)
avg_rating_location = df_clean.groupby('location')['rate'].mean().sort_values(ascending=False).head(10)
online_order_counts = df_clean['online_order'].value_counts()

# Visualizations
sns.set(style="whitegrid")

# Top 10 Cuisines
plt.figure(figsize=(10, 6))
sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette='viridis')
plt.title('Top 10 Cuisines')
plt.xlabel('Number of Restaurants')
plt.ylabel('Cuisine Type')
plt.tight_layout()
plt.show()

# Top 10 Locations by Restaurant Count
plt.figure(figsize=(10, 6))
sns.barplot(x=top_locations.values, y=top_locations.index, palette='mako')
plt.title('Top 10 Locations by Restaurant Count')
plt.xlabel('Number of Restaurants')
plt.ylabel('Location')
plt.tight_layout()
plt.show()

# Top Locations by Average Rating
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_rating_location.values, y=avg_rating_location.index, palette='coolwarm')
plt.title('Top Locations by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('Location')
plt.tight_layout()
plt.show()

# Online Order Availability
plt.figure(figsize=(6, 6))
online_order_counts.plot(kind='pie', autopct='%1.1f%%', colors=['#66c2a5', '#fc8d62'])
plt.title('Online Order Availability')
plt.ylabel('')
plt.tight_layout()
plt.show()

