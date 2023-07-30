#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Sample data
data = {
    'sales': [1000, 1200, 800],
    'profit': [200, 250, 150],
    'ship_mode': ['First Class', 'Same Day', 'Standard Class']
}

# Create DataFrame
df = pd.DataFrame(data)

# Define a function to calculate total_cost based on surcharge rules
def calculate_total_cost(row):
    if row['ship_mode'] == 'Same Day':
        return (row['sales'] - row['profit']) * 1.2
    elif row['ship_mode'] == 'First Class':
        return (row['sales'] - row['profit']) * 1.1
    elif row['ship_mode'] == 'Standard Class':
        return (row['sales'] - row['profit']) * 1.05
    else:
        return row['sales'] - row['profit']

# Apply the function to create the 'total_cost' column
df['total_cost'] = df.apply(calculate_total_cost, axis=1)

# Print the DataFrame with the new column
print(df)


# In[ ]:




