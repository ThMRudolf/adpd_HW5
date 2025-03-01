import pandas as pd
import pickle

# inference.py
"""
This script runs the model and estimates the house prices. the input data are the form test.csv.
"""

# Load the model
with open('/data/inference/house_pricing_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the test data
test_data = pd.read_csv('/data/raw/test.csv')

# Make predictions
predictions = model.predict(test_data)

# Save predictions to CSV
output_path = '/data/inference/predictions.csv'
pd.DataFrame(predictions, columns=['Predictions']).to_csv(output_path, index=False)

# Print confirmation
print(f"Predictions saved to {output_path}")