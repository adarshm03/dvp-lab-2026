import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. SETUP DATA
DATA_FILE = Path('Canada_Immigration.csv')
years = list(map(str, range(1980, 2014)))

# Load data
if DATA_FILE.exists():
    df = pd.read_csv(DATA_FILE)
    df.set_index('Country', inplace=True)
else:
    print("Error: Canada_Immigration.csv not found!")
    exit()

# Ensure years are numeric for plotting
df[years] = df[years].apply(pd.to_numeric)

# --- TASK 1: Area plot for top 6 immigrant countries (1990-2013) ---
years_1990_2013 = list(map(str, range(1990, 2014)))
df['Total_90_13'] = df[years_1990_2013].sum(axis=1)
top6_countries = df.sort_values(by='Total_90_13', ascending=False).head(6).index.tolist()
df_top6 = df.loc[top6_countries, years_1990_2013]

df_top6.T.plot(kind='area', figsize=(12, 6), stacked=True)
plt.title('Top 6 immigrant source countries (1990-2013)')
plt.xlabel('Year')
plt.ylabel('Number of immigrants')
plt.legend(title='Country')
plt.show()

# --- TASK 2: Bar chart for India (1980-2013) ---
df.loc['India', years].plot(kind='bar', figsize=(12, 5))
plt.title('Immigrants from India (1980-2013)')
plt.xlabel('Year')
plt.ylabel('Number of immigrants')
plt.show()

# --- TASK 3: Boxplot for India, Philippines, China ---
countries_box = ['India', 'Philippines', 'China']
df.loc[countries_box, years].T.plot(kind='box', figsize=(8, 6))
plt.title('Immigrants - India, Philippines, China (1980-2013)')
plt.ylabel('Number of immigrants')
plt.show()

# --- TASK 4: India vs France Area + Pie ---
pair_df = df.loc[['India', 'France'], years]

# Area Plot
pair_df.T.plot(kind='area', figsize=(12, 6), stacked=False)
plt.title('India and France immigrants (1980-2013)')
plt.xlabel('Year')
plt.ylabel('Number of immigrants')
plt.show()

# Pie Chart
pair_df.sum(axis=1).plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
plt.title('Total immigrants 1980-2013: India vs France')
plt.ylabel('')
plt.show()

# --- TASK 5: Scatter Fiji vs Singapore (Highlighting 2013) ---
x = df.loc['Fiji', years].values
y = df.loc['Singapore', years].values
years_int = list(map(int, years))

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Years 1980-2012')

# Annotate every 5 years + 2013
for xi, yi, yr in zip(x, y, years_int):
    if yr % 5 == 0 or yr == 2013:
        plt.annotate(str(yr), (xi, yi), textcoords="offset points", xytext=(3, 3), fontsize=8)

# Highlight 2013
idx2013 = years.index('2013')
plt.scatter(x[idx2013], y[idx2013], s=120, color='red', marker='o', label='2013')

plt.title('Fiji vs Singapore immigrants (1980-2013)')
plt.xlabel('Fiji')
plt.ylabel('Singapore')
plt.legend()
plt.show()