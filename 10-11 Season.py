import pandas as pd
import numpy as np

10-11_DF = pd.read_csv('/Users/brian/Documents/Premier_League/df_full_premierleague.csv',
                           usecols=['league_name','short_name','club_name','league_name','potential', 'overall','age','work_rate','nationality'], index_col=[1])
print(Fifa15_DF.head()) #top records
print(Fifa15_DF.dtypes) #dataframe data tyoes
