# my_lambdata/my_script.py

import pandas as pd
import datetime
import autopep8

from my_lambdata.split_date import convert_split_dates
from my_lambdata.add_column import add_column
from my_lambdata.cm import confusion_matrix

df = pd.read_csv('https://raw.githubusercontent.com/mtoce/Build2-Project/master/astros_bangs_20200127.csv')

df = convert_split_dates(df, 'game_date')

print(df['game_date'].dtype)

df = add_column(df, df['date_year'].tolist(), 'new_same_year')

print(df['date_hour'])

autopep8(my_lambdata.cm)