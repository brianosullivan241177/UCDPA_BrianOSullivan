# *********************** Brian O'Sullivan ***********************
# ********************* Irish Nationality ***********************
# *** Graphs comparing the best Irish players ***
# * https://github.com/brianosullivan241177/UCDPA_BrianOSullivan *

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project_Final/Modified/FIFAAllplayersM.csv',
                           usecols=['sofifa_id','short_name','long_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality_name','potential','dob','international_reputation'], index_col=[0])
print(FifaAll_Players_DF.head()) #top records
print(FifaAll_Players_DF.dtypes) #dataframe data tyoes

Irish_Nationality_DF = FifaAll_Players_DF[
    (FifaAll_Players_DF.nationality_name == 'Republic of Ireland')
   # & (FifaAll_Players_DF.league_name == 'English Premier League')
    & (FifaAll_Players_DF.overall >= 78)
]
print(Irish_Nationality_DF)


plot_order = Irish_Nationality_DF.sort_values(by=['Season'], inplace=True)
#
a = sns.catplot(data=Irish_Nationality_DF, x='Season',
                   y='overall', hue='long_name', height=6, aspect=2, order=plot_order, kind="point")

#
a = sns.catplot(data=Irish_Nationality_DF, x='Season',
                   y='wage_eur', hue='long_name', height=6, aspect=2, order=plot_order, kind="point")
plt.show()

top_irish_df = Irish_Nationality_DF.head(5)
print(top_irish_df)



Croatia_Nationality_DF = FifaAll_Players_DF[
    (FifaAll_Players_DF.nationality_name == 'Croatia')
   # & (FifaAll_Players_DF.league_name == 'English Premier League')
    & (FifaAll_Players_DF.overall >= 78)
]
print(Croatia_Nationality_DF)
#

plot_order = Croatia_Nationality_DF.sort_values(by=['Season'], inplace=True)
#
a = sns.catplot(data=Croatia_Nationality_DF, x='Season',
                   y='overall', hue='long_name', height=6, aspect=2, order=plot_order, kind="point")

#
a = sns.catplot(data=Croatia_Nationality_DF, x='Season',
                   y='wage_eur', hue='long_name', height=6, aspect=2, order=plot_order, kind="point")
plt.show()

top_Croatia_df = Croatia_Nationality_DF.head(5)
print(top_Croatia_df)
