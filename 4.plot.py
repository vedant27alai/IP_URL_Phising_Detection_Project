import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('processed_urlhaus_data.csv', low_memory=False)

# Print column names to verify
print("Column names in the DataFrame:", df.columns)

# Convert 'date_added' to datetime if the column exists
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df.set_index('date_added', inplace=True)
    
    # Plot the number of incidents per day
    daily_counts = df.resample('D').size()
    plt.figure(figsize=(12, 6))
    daily_counts.plot()
    plt.title('Number of Phishing Incidents per Day')
    plt.xlabel('Date')
    plt.ylabel('Number of Incidents')
    plt.grid(True)
    plt.show()
else:
    print("Column 'date_added' not found in the DataFrame.")
