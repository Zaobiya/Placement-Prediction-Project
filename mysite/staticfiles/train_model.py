import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('collegePlace.csv')

# Encode categorical variables
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# # Handle missing values
df = df.dropna()  # Drop rows with missing values, or use other methods for imputation

# # Perform one-hot encoding for 'Stream' column
df = pd.get_dummies(df, columns=['Stream'])

# # Split data into features and target variable
X = df.drop(columns=['PlacedOrNot', 'Age', 'Hostel'])
y = df['PlacedOrNot']

# # Train your model
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# # Serialize and save the model to a file
model_path = 'C:/Users/Zaobiya Khan/Desktop/PlacePred/model.pkl'

# Save the trained model
with open(model_path, 'wb') as f:
    pickle.dump(model, f)
