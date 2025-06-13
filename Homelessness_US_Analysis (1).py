#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyxlsb


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:



# Define the path to your downloaded .xlsb file

xlsb_file_path = '---'


# In[4]:


df = pd.read_excel(xlsb_file_path)
print("Excel file loaded successfully!")


# In[5]:


df.info()


# In[6]:


df.head()


# In[7]:


df.columns


# In[8]:


df.describe()


# In[9]:


df.shape


# In[12]:


df_filtered = df[pd.to_numeric(df['Overall Homeless'], errors='coerce').notna()]
df_filtered[['State','Overall Homeless']]


# In[28]:


df_filtered[['State', 'Overall Homeless']].sort_values('Overall Homeless', ascending = False).head(11)


# In[31]:


df_no_total = df_filtered[df_filtered['State'] != 'Total'].sort_values('Overall Homeless', ascending=False).head(10)


# In[40]:


# Visualizing the Chart 
plt.figure(figsize=(15, 8)) 

# Create the bar chart using Seaborn's barplot
ax = sns.barplot(
    x='State',
    y='Overall Homeless',
    data=df_no_total.head(10),
    palette='viridis' # Choose a color palette you like
)

# Add titles and labels for clarity
plt.title('10 States by Overall Homeless Population in 2024', fontsize=16)
plt.xlabel('State', fontsize=12)
plt.ylabel('Overall Homeless Count', fontsize=12)

# Rotate x-axis labels for better readability since there are many states
plt.xticks(rotation=45, ha='right', fontsize=10) # 'ha' aligns text to the right of the tick

# --- Add numbers on top of each bar ---
for container in ax.containers:
    ax.bar_label(container, fmt='%.0f', label_type='edge', fontsize=9, padding=3)
    # ax.bar_label(container, fmt='{:,.0f}', label_type='edge', fontsize=9, padding=3) # For comma separator

# Improve layout to prevent labels from overlapping
plt.tight_layout()

# Display the plot
plt.show()


# In[61]:


# Searching for Population Data of the States in 2024 and adding to the list and later to the DF
# I searched online from U.S. Census Bureau 2024 population estimates (latest available).

population_data = {
    'State': [
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI',
        'MN', 'MS', 'MO', 'MP', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
        'ND', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
        'VA', 'VI', 'VT', 'WA', 'WV', 'WI', 'WY', 'AS' # Included AS if you find a source for it, otherwise it will be NaN
    ],
    'Population 2024': [
        5157699, 740133, 7582384, 3088354, 39431263, 5957493, 3675069, 1051917,
        702250, 23372215, 11180878, 172951, # Guam 2024 est
        1446146, 2001619, 12710158, 6924275, 3241488, 2970606, 4588372, 4597740,
        1405012, 6263220, 7136171, 10140459, 5793151, 2943045, 6245466, 47326, # Northern Mariana Islands 2024 est
        1137233, 2005465, 3267467, 1409032, 9500851, 2130256, 19867248, 11046024,
        796568, 11883304, 4095393, 4272371, 13078751, 3203295, # Puerto Rico 2024 est
        1112308, 5478831, 924669, 7227750, 31290831, 3503613, 8811195, 98774, # U.S. Virgin Islands 2024 est
        648493, 7958180, 1769979, 5960975, 587618, 44293 # American Samoa 2024 est (from recent estimate)
    ]
}


# In[59]:


# Combining variables into one DF
df_population = pd.DataFrame(population_data)


# In[51]:


# Ensure 'State' column is a string type and strip any whitespace

df['State'] = df['State'].astype(str).str.strip()


# In[53]:



# Filter out non-state rows before merging
# Keep only rows where 'State' is a 2-letter abbreviation (typical for states/territories)
# and is not 'Total', 'NaN', or the descriptive text rows
df_cleaned = df[
    (df['State'].str.len() == 2) &
    (df['State'] != 'Total') &
    (df['State'] != 'nan') # 'nan' as a string if it wasn't already a numpy.nan
].copy() # .copy() to avoid SettingWithCopyWarning later


# In[54]:


# --- 3. Merge the population data with your cleaned DataFrame ---

df_merged = pd.merge(df_cleaned, df_population, on='State', how='left')

print("--- DataFrame after cleaning and merging Population 2024 (first 10 rows) ---")
print(df_merged.head(10))
print(f"\nShape of merged DataFrame: {df_merged.shape}")


# In[68]:


df_homeless_pop = df_merged[['State', 'Overall Homeless', 'Population 2024']].sort_values('Population 2024', ascending = False).head(10)
df_homeless_pop 


# In[ ]:




