import pandas as pd
import datetime

def convert_split_dates(X, column):
    '''
    Converts an object column into a datetime dtype.
    Then creates columns for year, month and day.
    Input: dataframe, column of dataframe you plan to convert / create new columns with
    Output: dataframe with new columns
    '''
    
    X = X.copy()

    # create a boolean index to see if our column is the correct type
    if (X[column].dtype == 'O'):
        X[column] = pd.to_datetime(X[column], infer_datetime_format=True)
        # if the column type is correct, simply create new cols
        X['date_year'] = X[column].dt.year
        X['date_month'] = X[column].dt.month
        X['date_day'] = X[column].dt.day
    else:
       print("The type of your column is not an object, datetime, or timestamp.")

    return X