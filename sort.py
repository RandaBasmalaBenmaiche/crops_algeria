import pandas as pd

# Load data from CSV file
df = pd.read_csv('updated_file.csv')

# Ensure that the 'month' column is treated as integers
df['month'] = pd.to_numeric(df['month'], errors='coerce', downcast='integer')

# Sort the data by 'year' and 'month' columns, treating month as an integer
sorted_df = df.sort_values(by=['year', 'month'], ascending=[True, True])

# Save the sorted data to a new CSV file
sorted_df.to_csv('sorted_data.csv', index=False)

print("Data has been sorted and saved to 'sorted_data.csv'")
