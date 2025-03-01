# predict_house_prices.py
"""
This module contains functions to prepare, build, train/fit, predict and validate
a model, that predicts house prices.
functions:
- prepare_train_data(train)
- build_model_estimate_house_pricing(numerical_cols, categorical_cols)
- predict_and_evaluate_estimation_house_pricing(pipeline, x_valid, y_valid)
- split_train_data_for_estimate_house_pricing(x, y)
- validate_house_pricing_model(pipeline, x_valid, y_valid)
- test_house_pricing_model(pipeline, test, sample)
- select_numerical(df)
- select_categorical(df)
"""

# libraries for data analysis
import pandas as pd
t
# libararies for estimation model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error

# Separate target variable and features
# drop 'SalePrice' column from input matrix and define it as output vector y
def prepare_train_data(train):
    """
    Prepares the data for training by separating the target variable and features,
    and identifying numerical and categorical columns.

    Params:
        train: Training data.

    Returns:
        X: Features.
        y: Target variable.
        numerical_cols: List of numerical columns.
        categorical_cols: List of categorical columns.
    """
    x = train.drop('SalePrice', axis=1)
    y = train['SalePrice']
    numerical_cols = select_numerical(x).columns
    categorical_cols = select_categorical(x).columns
    return x, y, numerical_cols, categorical_cols

def build_model_estimate_house_pricing(numerical_cols, categorical_cols):
    """
    Builds the preprocessing pipeline and the model.

    Params:
        numerical_cols: List of numerical columns.
        categorical_cols: List of categorical columns.

    Returns:
        pipeline: A pipeline with preprocessing and model.
    """
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])

    model = RandomForestRegressor(n_estimators=100, random_state=0)

    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('model', model)
                              ])
    return pipeline

def validate_estimation_house_pricing(pipeline, x_valid, y_valid):
    """
    Makes predictions and evaluates the model.

    Params:
        pipeline: The fitted pipeline.
        X_valid: Validation features.
        y_valid: Validation target variable.

    Returns:
        preds: Predictions.
        mae: Mean Absolute Error.
        mape: Mean Absolute Percentage Error.
    """
    preds = pipeline.predict(x_valid)
    mae = mean_absolute_error(y_valid, preds)
    mape = mean_absolute_percentage_error(y_valid, preds)
    return preds, mae, mape

def split_train_data_for_estimate_house_pricing(x, y):
    """
    Estimates the house price depending on different inputs.

    Params:
        train: Train data.
        test: Test data.
        sample: Sales prices of test data.

    Returns:
        Returns a DataFrame that contains the estimated price, 
        the real price of the test data houses, and the absolute
        and percentage differences of real value and estimated values.
    """


    x_train, x_valid, y_train, y_valid = train_test_split(x,
                                                          y,
                                                          train_size=0.8,
                                                          test_size=0.2,
                                                          random_state=0)
    return x_train, x_valid, y_train, y_valid

def fit_house_pricing_models(pipeline,
                             x_train,
                             y_train
                             ):
    """
    fits the house price depending on different inputs.

    Params:
        pipeline: build model for house price estimation.
        x_train: input data to train/fit the model
        y_train: output data to train/fit the model

    Returns:
        Returns a fitted model (pipeline) to estimated price, 
    """
    pipeline.fit(x_train, y_train)
    return pipeline

def validate_house_pricing_model(pipeline,
                                x_valid,
                                y_valid):
    """
        Validate the fitted model with validation data and
        prints: Mean Absolute Error,Mean Absolute Percentage Error and 
        predicted valuesfits the house price depending on different inputs.

    Params:
        pipeline: build model for house price estimation.
        x_valid: input data to validate the model
        y_valid: output data to validate the model

    Returns: no return values, just prints.

    """
    preds, mae, mape = predict_and_evaluate_estimation_house_pricing(pipeline, x_valid, y_valid)
    print('Mean Absolute Error:', mae)
    print('Mean Absolute Percentage Error:', mape)
    print('predicted values:', preds)

def test_house_pricing_model(pipeline,
                              test,
                              sample):
    """
        Tests the fitted and validated model with test data and
        and make a prediction for a sample
 
    Params:
        pipeline: build model for house price estimation.
        test: Test data.
        sample: Sales prices of test data.

    Returns: no return values, just prints.
    """
    test_preds = pipeline.predict(test.drop('Id', axis=1))
    submission = pd.DataFrame({
        'SalePrice pred': test_preds,
        'SalePrice': sample['SalePrice'],
        'diff SalePrice': sample['SalePrice'] - test_preds,
        'percentage diff SalePrice': (sample['SalePrice'] - test_preds) / sample['SalePrice'] * 100
    })

    return submission

def select_numerical(df):
    """
    Selects only numerical columns from the DataFrame.

    Params:
        df: DataFrame from which numerical columns are to be selected.

    Returns:
        DataFrame containing only numerical columns.
    """
    numerical_df = df.select_dtypes(include=['int64', 'float64'])
    return numerical_df

def select_categorical(df):

    """
    Selects only categorical columns from the DataFrame.

    Params:
        df: DataFrame from which categorical columns are to be selected.

    Returns:
        DataFrame containing only categorical columns.
    """
    categorical_df = df.select_dtypes(include=['object'])
    return categorical_df

def save_prep_data_2_prep(df, name):
    """
    Takes a DataFrame and tne name. The df is separeted in 
    x and y data and numercial and categorical values.

    Params:
        df: DataFrame from which categorical columns are to be selected.
        name: 'train' or 'test'

    Returns:
        no return values. Saves the DataFrame for train, test and the 
        numerical and categorical information to ../data/prep
    """
    x_df, y_df, numerical_cols, categorical_cols = prepare_train_data(df)
    print(numerical_cols)
    x_df.to_csv(f'../data/prep/x_{name}.csv', index=False)
    y_df.to_csv('../data/prep/y_train.csv', index=False)
    # Save numerical columns to a file
    with open(f'../data/prep/numerical_cols_{name}n.txt', 'w') as f:
        for col in numerical_cols:
            f.write(f"{col}\n")
    with open(f'../data/prep/categorical_cols_{name}.txt', 'w') as f:
        for col in categorical_cols:
            f.write(f"{col}\n")
