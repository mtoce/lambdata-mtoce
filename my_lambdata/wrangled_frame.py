# my_lambdata/state_abbrev.py

from pandas import DataFrame

# df = pd.DataFrame()

# pd.DataFrame

from pandas import DataFrame
class WrangledFrame(DataFrame):
    """
    A custom pandas.DataFrame with a column called "abbrev"
    Example: WrangledFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    """
    def add_state_names(self):
        """
        Converts a dataframe with a column of state abbreviations, adding a corresponding column of state names.
        H/T: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        """
        names_map = {"CA": "Cali", "CO": "Colo",
                    "CT": "Conn", "DC": "District of Columbia"}
        self["name"] = self["abbrev"].map(names_map)
    def inspect_columns(self):
        print(self.columns)
if __name__ == "__main__":
    # df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    # print(df.head())
    # df2 = add_state_names(df)
    # print(df2.head())
    # df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    # print(df.head())
    # wrangler = Wrangler(df)
    # print(type(wrangler))
    # wrangler.inspect_columns()
    # #df2 = wrangler.add_state_names()
    # #print(df2.head())
    # wrangler.add_state_names()
    # print(wrangler.df.head())
    wf = WrangledFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(wf.head())
    wf.add_state_names()
    print(wf.head())
    wf.inspect_columns()