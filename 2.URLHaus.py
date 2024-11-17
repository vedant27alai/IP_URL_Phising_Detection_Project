import csv

# Path to the URLhaus text file
file_path = 'csv.txt'
output_file = 'processed_urlhaus_data.csv'

# Initialize lists to store data
malware_sites = []

# Read and process the data
with open(file_path, 'r', encoding='utf-8') as file:
    # Skip the header lines
    for _ in range(5):  # Adjust this if necessary
        next(file)
    
    # Read the CSV data
    reader = csv.reader(file)
    header = next(reader)  # Read the header row
    
    for row in reader:
        # Strip quotes from fields
        row = [field.strip('"') for field in row]
        
        # Ensure the row has the expected number of fields
        if len(row) >= 9:
            # Extract relevant fields
            malware_sites.append({
                'id': row[0],
                'date_added': row[1],
                'url': row[2],
                'status': row[3],
                'last_online': row[4],
                'threat': row[5],
                'tags': row[6],
                'urlhaus_link': row[7],
                'reporter': row[8]
            })

# Write the processed data to a CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'date_added', 'url', 'status', 'last_online', 'threat', 'tags', 'urlhaus_link', 'reporter'])
    writer.writeheader()
    writer.writerows(malware_sites)

print(f"Data saved to {output_file}")
