"""
    Main script to prepare data, train a model, and validate.
    This script performs the following steps:
    1. Reads raw data from CSV files.
    2. Prepares the training data by processing and splitting it.
    3. Saves the prepared data to the 'data/prep' directory.
    4. Builds and trains a house pricing estimation model.
    Modules:
        logging: For logging errors and debug information.
        src.prep: Contains functions for data preparation.
        src.train: Contains functions for model building and training.
    Constants:
        TRAIN_LOC_STR (str): File path for the training data CSV.
        TEST_LOC_STR (str): File path for the test data CSV.
        SUBSAMPLES_LOC_STR (str): File path for the sample submission CSV.
        NAME (str): Name used in logging format.
    Functions:
        read_data: Reads data from a CSV file.
        prepare_train_data: Prepares the training data.
        split_train_data: Splits the data into training and validation sets.
        save_prep_data_2_prep: Saves prepared data to a specified location.
        save_col_name: Saves column names to a file.
        build_model_estimate_house_pricing: Builds a model for house pricing estimation.
        fit_house_pricing_models: Fits the house pricing model to the training data.
    Exceptions:
        Logs any exceptions that occur during data reading, preparation, splitting, saving, and model building/fitting.
    main to prepare data, train a model and validate.
"""
# import general
import logging
# import modules
from src.prep import (read_data,
                      prepare_train_data,
                      split_train_data,
                      save_prep_data_2_prep,
                      save_col_name, 
                      handle_missing_values)
from src.train import (build_model_estimate_house_pricing,
                       fit_house_pricing_models,
                       estimation_test,
                       validate_estimation_house_pricing)

#
if __name__ == "__main__":
    RAIN_LOC_STR = 'data/raw/train.csv'
    TEST_LOC_STR = 'data/raw/test.csv'
    SUBSAMPLES_LOC_STR = 'data/raw/sample_submission.csv'

    # definition log file
    logging.basicConfig(
        filename='./logs/results.log',
        level=logging.DEBUG,
        filemode='w',
        format=f'%(name)s .%(levelname)s - %(message)s')
    # Read all data
    try:
        train_df = read_data(TRAIN_LOC_STR)
        test_df = read_data(TEST_LOC_STR)
        sample_df = read_data(SUBSAMPLES_LOC_STR)
    except Exception as e_read_raw:
        logging.error(f"Exception occurred during data allocation: {e_read_raw}")
        logging.debug(e_read_raw)
    ## prepare data

    # handle missing data
    try:
        train_df = handle_missing_values(train_df)
        test_df = handle_missing_values(test_df)
        sample_df = handle_missing_values(sample_df)
    except Exception as e:
        logging.error(f"Error occurred during hanlding missing datan: {e}")
        logging.debug(e)   
    # prep train data
    try:
        x, y = prepare_train_data(train_df, 'SalePrice')
    except Exception as e:
        logging.error(f"Error occurred during data preparation: {e}")
        logging.debug(e)
    # split data
    try:
        x_train, x_valid, y_train, y_valid=split_train_data(x, y)
    except Exception as e:
        logging.error(f"Error occurred during data split: {e}")
        logging.debug(e)
    # save data in data/prep
    # x_train data
    try:
        save_prep_data_2_prep(x_train, 'x_train')
    except Exception as e:
        logging.error(f"Error occurred during data saving x_train: {e}")
        logging.debug(e)
    # y_train data
    try:
        save_prep_data_2_prep(y_train, 'y_train')
    except Exception as e:
        logging.error(f"Error occurred during data saving y_train: {e}")
        logging.debug(e)
    # x_valid data
    try:
        save_prep_data_2_prep(x_valid, 'x_valid')
    except Exception as e:
        logging.error(f"Error occurred during data saving x_valid: {e}")
        logging.debug(e)
    # y_valid data
    try:
        save_prep_data_2_prep(y_valid, 'y_valid')
    except Exception as e:
        logging.error(f"Error occurred during data saving y_valid: {e}")
        logging.debug(e)
    # y_valid data
    #try:
        #save_col_name(numerical_cols, categorical_cols, 'train')
    #except Exception as e:
    #    logging.error(f"Error occurred during data saving y_valid: {e}")
    #    logging.debug(e)

    #
    # Model build and training
    X_TRAIN_LOC_STR = 'data/prep/x_train.csv'
    X_VALID_LOC_STR = 'data/prep/x_valid.csv'
    Y_TRAIN_LOC_STR = 'data/prep/y_train.csv'
    Y_VALID_LOC_STR = 'data/prep/y_valid.csv'
    # read data
    x_train = read_data(X_TRAIN_LOC_STR)
    x_valid = read_data(X_VALID_LOC_STR)
    y_train = read_data(Y_TRAIN_LOC_STR)
    y_valid = read_data(X_VALID_LOC_STR)
    # Read numerical columns
    #try:
    #    with open('data/prep/numerical_cols_train.txt', 'r') as file:
    #        num_cols = file.read().splitlines()
    #except Exception as e:
    #    logging.error(f"Error occurred during reading numerical columns: {e}")
    #    logging.debug(e)#

    #try:
    #    with open('data/prep/categorical_cols_train.txt', 'r') as file:
    #        cat_cols = file.read().splitlines()
    #except Exception as e:
    #    logging.error(f"Error occurred during reading numerical columns: {e}")
    #    logging.debug(e)

    try:
        my_pipeline = build_model_estimate_house_pricing(x_train)
    except Exception as e:
        logging.error(f"Error occurred during model build: {e}")
        logging.debug(e)

    try:
        my_pipeline_fitted = fit_house_pricing_models(my_pipeline,
                                x_train,
                                y_train
                                )
    except Exception as e:
        logging.error(f"Error occurred during model fit: {e}")
        logging.debug(e)

    try:
        print('test --------:')
        xt = test_df 
        yt = sample_df
        estimation_test(my_pipeline_fitted,
                                xt,
                                yt
                                )
    except Exception as e:
        logging.error(f"Error occurred during test model: {e}")
        logging.debug(e)

    try:
        my_pipeline_valid = validate_estimation_house_pricing(my_pipeline_fitted,
                                x_valid,
                                y_valid
                                )
        print('pipeline validated.')
    except Exception as e:
        print(e)
        logging.error(f"Error occurred during model validation: {e}")
        logging.debug(e)