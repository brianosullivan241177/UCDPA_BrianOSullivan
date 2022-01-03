import os, glob
import pandas as pd
import numpy as np
import seaborn as sns

Fifa15_DF = pd.read_csv('/Users/brian/Documents/FIFA_Project/players_15.csv',
                           usecols=['league_name','short_name','club_name','league_name','potential', 'overall','age','work_rate','nationality'], index_col=[1])
print(Fifa15_DF.head()) #top records
print(Fifa15_DF.dtypes) #dataframe data tyoes

#Premier_League = Fifa15_DF.loc["English Premier League"]
English_PL_DF = Fifa15_DF[(Fifa15_DF.league_name == 'English Premier League') & ((Fifa15_DF.club_name == 'Hull City') | (Fifa15_DF.club_name == 'Burnley') | (Fifa15_DF.club_name == 'Queens Park Rangers'))] #Premier League players
print(English_PL_DF) #Premier League top records
