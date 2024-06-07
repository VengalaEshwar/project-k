import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import joblib
from sklearn.metrics import accuracy_score
from joblib import dump, load

#-----------------------------------------------------------------------------------
#                           DATA PREPROCESSING

# Load the dataset
df = pd.read_csv("parkinsons.csv")

# Check for null values
print("Null values per column before dropping any rows:")
print(df.isnull().sum())

# Convert numeric columns to numeric data types (coercing errors to NaN)
numeric_columns = df.columns[1:]  # excluding 'name' column
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Drop rows with any missing values
df.dropna(inplace=True)

# Separate features and target
x = df.drop("status", axis=1)
y = df["status"]

# Drop the 'name' column as it is not a feature
x = x.drop("name", axis=1)

# Check for non-numeric values
print("Data types after conversion:")
print(x.dtypes)

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Data scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#----------------------------------------------------------------------------------
#                                 DEEP LEARNING
# Define the model
model = Sequential()
model.add(Dense(64, input_dim=x_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=60, batch_size=10, validation_data=(x_test, y_test))

# Save the model and the scaler
model.save('deep_learning_model.h5')
joblib.dump(scaler, 'scaler.joblib')

print("Model and scaler saved successfully.")

# Make predictions on the test set
y_pred_prob = model.predict(x_test)
y_pred = (y_pred_prob >= 0.5).astype(int)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy on test set: {accuracy * 100:.2f}%")
