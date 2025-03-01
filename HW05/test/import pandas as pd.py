import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

def build_price_estimation_model(data):
    # Separate features and target
    X = data.drop('price', axis=1)
    y = data['price']
    
    # Identify numerical and categorical columns
    numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = X.select_dtypes(include=['object']).columns
    
    # Preprocessing for numerical data
    numerical_transformer = StandardScaler()
    
    # Preprocessing for categorical data
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')
    
    # Bundle preprocessing for numerical and categorical data
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])
    
    # Define the model
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    
    # Create and evaluate the pipeline
    clf = Pipeline(steps=[('preprocessor', preprocessor),
                          ('model', model)])
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    # Fit the model
    clf.fit(X_train, y_train)
    
    # Return the trained model
    return clf