# *********************** Brian O'Sullivan ***********************
# ********************* Golden Boy Winners ***********************
# *** Graphs comparing the Golden Boy winners ***
# * https://github.com/brianosullivan241177/UCDPA_BrianOSullivan *
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from bokeh.io import show

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project_Final/Modified/FIFAAllplayersM.csv',
                           usecols=['sofifa_id','short_name','long_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','weight_kg','nationality_name','potential','dob','club_position'], index_col=[0])
print(FifaAll_Players_DF.head()) #top records
print(FifaAll_Players_DF.dtypes) #dataframe data tyoes

Season_2014_2015_DF = FifaAll_Players_DF[
    (FifaAll_Players_DF.Season == '2014-2015')]


Who_is_like_Salah_DF = Season_2014_2015_DF[
    (Season_2014_2015_DF.club_position == 'SUB')
    & (Season_2014_2015_DF.potential == 84)
    & (Season_2014_2015_DF.overall == 76)
]
print(Who_is_like_Salah_DF)

Could_be_like_Salah_DF = FifaAll_Players_DF=FifaAll_Players_DF[
    (FifaAll_Players_DF.short_name== 'M. van Ginkel')
    | (FifaAll_Players_DF.short_name== 'T. Hazard')
    | (FifaAll_Players_DF.short_name== 'Dória')
    | (FifaAll_Players_DF.short_name == 'M. Salah')
]

plot_order = Could_be_like_Salah_DF.sort_values(by=['Season'], inplace=True)
Could_be_like_Salah_DF.rename(columns = {'overall':'Overall Rating in %', 'wage_eur':'Wages paid in Euro',
                                     'long_name':'Player Name'}, inplace = True)
a = sns.catplot(data=Could_be_like_Salah_DF, x='Season',
                   y='Overall Rating in %', hue='Player Name', height=5, aspect=2, order=plot_order, kind="point")
plt.title("Players like Salah in 2014 and how they compared over the seasons")
plt.xlabel("Season")
plt.ylabel("Overall Rating in %")
plt.show()





