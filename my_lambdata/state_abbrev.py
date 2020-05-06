# my_lambdata/state_abbrev.py

from pandas import DataFrame

# df = pd.DataFrame()

# pd.DataFrame


def add_state_names(my_df):
    '''
    Converts a dataframe with a column of state abbreviations, adding corresponding column of state names

    Params: 
        my_df - a pandas.DataFrame with a column called "abbrev". 

    Example:
        DataFrame({"abbrev":["CA", "CO", "CT", "DC", "TX"]})
    '''
    # state abbreviation -> Full Name and vice versa.
    # FL -> Florida, etc.

    new_frame = my_df.copy()
    # need list or dict with the abbrev/name mappings
    names_map = {"CA": "California", "CO": "Colorado",
                 "CT": "Connecticut", "DC": "District of Columbia", "TX": "Texas"}

    # create a new column which maps the existing column using our names map
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    new_frame['name'] = new_frame['abbrev'].map(names_map)

    breakpoint()

    return new_frame


if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())
