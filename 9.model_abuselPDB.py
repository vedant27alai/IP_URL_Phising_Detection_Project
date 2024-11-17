import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import pickle

# Load your dataset
df = pd.read_csv('combined_abuseipdb_data.csv', low_memory=False)

# Define labels based on 'target' column (assuming it contains 'safe' or 'unsafe')
# If your target column has different labels, adjust the mapping accordingly
df['label'] = df['target'].apply(lambda x: 'safe' if x == 'safe' else 'unsafe')

# Use only the 'ipAddress' column for features
X = df['ipAddress']
y = df['label']

# Create a pipeline with CountVectorizer and RandomForestClassifier
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),  # Converts text data into numerical features
    ('classifier', RandomForestClassifier())  # Classification model
])

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
pipeline.fit(X_train, y_train)

# Save the trained model
with open('ip_detection_model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)

# Print the accuracy on the test set
accuracy = pipeline.score(X_test, y_test)
print(f'Model accuracy: {accuracy:.2f}')
