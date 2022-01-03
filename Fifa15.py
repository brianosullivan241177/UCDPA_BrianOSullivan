import os, glob
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


Fifa15_DF = pd.read_csv('/Users/brian/Documents/FIFA_Project/players_15.csv',
                           usecols=['league_name','short_name','club_name','wage_eur','league_name','preferred_foot', 'overall','age','work_rate','nationality'], index_col=[1])
print(Fifa15_DF.head()) #top records
print(Fifa15_DF.dtypes) #dataframe data tyoes



English_PL_Relegated_20142015_DF = Fifa15_DF[(Fifa15_DF.league_name == 'English Premier League') & ((Fifa15_DF.club_name == 'Hull City')
                                                                                           | (Fifa15_DF.club_name == 'Burnley')
                                                                                           | (Fifa15_DF.club_name == 'Queens Park Rangers'))] #Premier League players
print(English_PL_Relegated_20142015_DF) #Premier League relegated players - top records


print("********************** 2014 - 2015 Escaped Relegation - Start **********************")
English_PL_Escaped_Relegation_20142015_DF=Fifa15_DF[(Fifa15_DF.league_name == 'English Premier League') & ((Fifa15_DF.club_name == 'Newcastle United')
                                                                                                  | (Fifa15_DF.club_name == 'Sunderland')
                                                                                                  | (Fifa15_DF.club_name == 'Aston Villa'))] #Premier League players
print(English_PL_Escaped_Relegation_20142015_DF) #Premier League escaped relegatio players - top records
print("********************** 2014 - 2015 Escaped Relegation - End **********************")

Feet_Type = English_PL_Relegated_20142015_DF.preferred_foot.value_counts()
print(Feet_Type)

def as_thousands(value):
    return value / 10_000
English_PL_Escaped_Relegation_20142015_DF[['wage_eur','club_name']].groupby('club_name') \
                                            .sum() \
                                            .sort_values('wage_eur', ascending=False) \
                                            .head(10) \
                                            .apply(as_thousands) \
                                            .plot(kind='bar', figsize=(11,6))

plt.xlabel("")
plt.ylabel('Salary')
plt.title('Weekly Salary in Thousands - Escaped Relegation');
plt.show()


English_PL_Relegated_20142015_DF[['wage_eur','club_name']].groupby('club_name') \
                                            .sum() \
                                            .sort_values('wage_eur', ascending=False) \
                                            .head(10) \
                                            .apply(as_thousands) \
                                            .plot(kind='bar', figsize=(11,6))

plt.xlabel("")
plt.ylabel('Salary')
plt.title('Weekly Salary in Thousands - Relegated');
plt.show()

