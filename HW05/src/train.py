# train.py
"""
This script calls the train data and builds, fits and tests the model.
The train and fitted model is then stored in /data/inference as house_price_model.pkl
"""
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
import numpy as np
import pandas as pd

# builds model
def build_model_estimate_house_pricing(x):
    """
    Builds the preprocessing pipeline and the model.

    Args: 
        x (dataframe): DataFrame containing the features.

    Returns:
        pipeline: A pipeline with preprocessing and model.
    """

    # Identify numerical and categorical features
    num_features = x.select_dtypes(include=['int64', 'float64']).columns
    cat_features = x.select_dtypes(include=['object']).columns

    num_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    cat_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))#('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", num_pipeline, num_features),
        ("cat", cat_pipeline, cat_features)
    ])


    model = RandomForestRegressor(n_estimators=100, 
                                  random_state=0)

    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('model', model)
                              ])
    return pipeline

# fits model with train data
def fit_house_pricing_models(pipeline,
                             x_train,
                             y_train
                             ):
    """
    fits the house price depending on different inputs.

    Args: 
        pipeline (sklearn pipeline): build model for house price estimation.
        x_train (dataframe): input data to train/fit the model
        y_train (dataframe): output data to train/fit the model

    Returns:
        Returns a fitted model (pipeline) to estimated price, 
    """
    # Ensure y_train is in the shape (n_samples,)
    if len(y_train.shape) > 1 and y_train.shape[1] == 1:
        y_train = np.ravel(y_train) #pd.DataFrame(np.ravel(y_train))
    pipeline.fit(x_train, y_train)
    
    return pipeline
# test model
def estimation_test(pipeline, x, y):
    """
    test the fitted model
    Args: 
        pipeline (sklearn pipeline): model for house price estimation.
        df (dataframe): test data 
        target_str (str): variable to be estimated, "SalePrice"
    Return: no return data, just a model score value.
    """
    print("model score: %.3f" % pipeline.score(x, y))
# validates model   
def validate_estimation_house_pricing(pipeline, x_valid, y_valid):
    """
    Makes predictions and evaluates the model.

    Args:
        pipeline (sklearn pipeline): The fitted pipeline.
        X_valid (dataframe): Validation features.
        y_valid (dataframe): Validation target variable.

    Returns:
        preds: Predictions.
        mae: Mean Absolute Error.
        mape: Mean Absolute Percentage Error.
    """
    preds = pipeline.predict(x_valid)
    mae = mean_absolute_error(y_valid, preds)
    mape = mean_absolute_percentage_error(y_valid, preds)
    return preds, mae, mape


