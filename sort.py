import pandas as pd

# Load data from CSV file
df = pd.read_csv('test/sorted_data.csv')


sorted_df = df.sort_values(by=['year','month'], ascending=[True,True])

# Save the sorted data to a new CSV file
sorted_df.to_csv('test/sorted_data.csv', index=False)

print("Data has been sorted and saved to 'sorted_data.csv'")
