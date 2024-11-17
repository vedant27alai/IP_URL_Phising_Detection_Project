import pandas as pd

# Load the CSV file, skipping the first row if it contains header info
df = pd.read_csv(
    'processed_urlhaus_data.csv',
    skiprows=[0],  # Skip the first row if it is not a data row
    dtype={'# id': str}  # Ensure '# id' is treated as a string
)

# Print the column names
print("Column names in the DataFrame:", df.columns)

# Print the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Convert 'dateadded' to datetime format
df['dateadded'] = pd.to_datetime(df['dateadded'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Convert 'last_online' to datetime format if it's not already
df['last_online'] = pd.to_datetime(df['last_online'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Display the DataFrame info
print("DataFrame Info:")
print(df.info())
