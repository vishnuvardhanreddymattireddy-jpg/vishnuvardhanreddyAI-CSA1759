import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text
import os

# --- Load CSV file ---
file_path = "play_tennis.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print(f"Successfully loaded {file_path}:")
else:
    print(f"Warning: '{file_path}' not found. Creating a sample DataFrame for demonstration.")
    # Create a sample DataFrame if the file is not found
    data = {
        'outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
        'temp': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
        'humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
        'wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
        'play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
    }
    df = pd.DataFrame(data)

print("Dataset:\n", df)

# --- Label Encoding ---
le_dict = {}

for column in df.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    le_dict[column] = le

# Features and Target
X = df.drop('play', axis=1)
y = df['play']

# --- Train Decision Tree ---
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

# --- Print Decision Tree Rules ---
print("\nDecision Tree Rules:")
print(export_text(model, feature_names=list(X.columns)))

# --- Example Prediction ---
sample = {
    'outlook': le_dict['outlook'].transform(['Sunny'])[0],
    'temp': le_dict['temp'].transform(['Mild'])[0],
    'humidity': le_dict['humidity'].transform(['High'])[0],
    'wind': le_dict['wind'].transform(['Weak'])[0]
}

sample_df = pd.DataFrame([sample])

prediction = model.predict(sample_df)[0]

# Convert prediction back to Yes/No
result = le_dict['play'].inverse_transform([prediction])[0]

print("\nPrediction:", result)
