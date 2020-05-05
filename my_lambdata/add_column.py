import pandas as pd

def add_column(X, new_feature, new_feature_name):
    '''
    Takes list and converts to series and adds as column to dataframe.
    Input: dataframe, feature (type=list)
    '''
    if len(new_feature) == X.shape[0]:
        new_col = pd.Series(new_feature)
        X[new_feature_name] = new_col
    else:
        print("your list is the wrong length for this shape of dataframe, homie.")
    return X