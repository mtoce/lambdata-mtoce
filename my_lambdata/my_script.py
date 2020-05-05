# my_lambdata/my_script.py

import pandas as pd
import datetime

from my_lambdata.mod1 import convert_split_dates

df = pd.read_csv('https://raw.githubusercontent.com/mtoce/Build2-Project/master/astros_bangs_20200127.csv')

convert_split_dates(df, df['game_date'])