import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import pickle

# Load your dataset
df = pd.read_csv('processed_urlhaus_data.csv', low_memory=False)  # Set low_memory=False to avoid dtype warnings

# Check if 'label' column exists; if not, create it for demonstration purposes
# For real use, make sure 'label' is properly created based on your data
if 'label' not in df.columns:
    # Example logic: This is just a placeholder; you should replace it with actual logic to define labels
    df['label'] = df['status'].apply(lambda x: 'safe' if x == 'safe' else 'not_safe')

# Split the dataset into features and labels
X = df['url']
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
with open('fraud_detection_model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)

# Print the accuracy on the test set
accuracy = pipeline.score(X_test, y_test)
print(f'Model accuracy: {accuracy:.2f}')
