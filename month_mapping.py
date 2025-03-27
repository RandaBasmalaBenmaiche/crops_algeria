import pandas as pd

# Function to map French month names to numbers
def month_to_number(month_name):
    # Dictionary mapping month names in French to their corresponding numbers
    month_mapping = {
        "janvier": 1,
        "février": 2,
        "feévrier":2,
        "fevrier":2,
        "mars": 3,
        "avril": 4,
        "mai": 5,
        "mali":5,
        "juin": 6,
        "juillet": 7,
        "août": 8,
        "aoiit":8,
        "aoiut":8,
        "aout":8,
        "septembre": 9,
        "octobre": 10,
        "novembre": 11,
        "décembre": 12,
        "déecembre":12,
        'decembre':12
    }

    # Convert the month name to lowercase to handle case-insensitive matching
    month_name_lower = month_name.strip().lower()

    # Return the corresponding month number or "Mois invalide" if invalid
    return month_mapping.get(month_name_lower, "Mois invalide")

# Read the CSV file into a DataFrame
df = pd.read_csv('testOCR.csv')

# Assuming the CSV has a column named 'month' with French month names
# Apply the function to map the French month names to numbers
df['month'] = df['month'].apply(month_to_number)

# Write the updated DataFrame back to a new CSV file
df.to_csv('updated_file.csv', index=False)

print("Month names have been converted and saved to 'updated_file.csv'.")
