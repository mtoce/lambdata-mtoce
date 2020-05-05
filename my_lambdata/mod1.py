import pandas as pd
import datetime

def convert_split_dates(X, column):
    '''
    Converts a date column into additional columns of: Year, Month, and Day
    Input: dataframe, column of dataframe you plan to convert / create new columns with
    Output: dataframe with new columns
    '''
    
    X = X.copy()

    # create a boolean index to see if our column is the correct type
    if type(column) == object:
        column = pd.to_datetime(column, infer_datetime_format=True)
    # if the column type is correct, simply create new cols
    elif (type(column) == datetime.datetime) | (type(column) == pd.Timestamp):
        X['date_year'] = X['column'].dt.year
        X['date_month'] = X['column'].dt.Month
        X['date_day'] = X['column'].dt.day
        return X
    else:
        try_again = print("The type of your column is not an object, datetime, or timestamp.")
        return try_again
        