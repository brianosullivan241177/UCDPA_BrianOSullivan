# *********************** Brian O'Sullivan ***********************
# ********************* Golden Boy Winners ***********************
# *** Graphs comparing the Golden Boy winners ***
# * https://github.com/brianosullivan241177/UCDPA_BrianOSullivan *

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/FIFAAllplayers_GB.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential'], index_col=[0])
print(FifaAll_Players_DF.head()) #top records
print(FifaAll_Players_DF.dtypes) #dataframe data tyoes

FifaAll_Players_DF.rename(columns = {'overall':'Overall Rating in %', 'wage_eur':'Wages paid in Euro'}, inplace = True)

Golden_Boy_Winners_DF = FifaAll_Players_DF[
    (FifaAll_Players_DF.short_name == 'GB Winner 2010 M. Balotelli')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2011 M. Götze')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2012 Isco')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2013 P. Pogba')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2014 R. Sterling')
]
print(Golden_Boy_Winners_DF)

plot_order = Golden_Boy_Winners_DF.sort_values(by=['Season'], inplace=True)
# Graph to show overall ratings by Golden Boy winner - R. Sterling continuing to improve
a = sns.catplot(data=Golden_Boy_Winners_DF, x='Season',
                   y='Overall Rating in %', hue='short_name', height=6, aspect=2, order=plot_order, kind="point")
a.fig.suptitle('Golden Boy Winners Overall ratings in % per Season')

# Graph to show wages by Golden Boy winner R. Sterling getting better wages
a1 = sns.catplot(data=Golden_Boy_Winners_DF, x='Season',
                   y='Wages paid in Euro', hue='short_name', height=6, aspect=2, order=plot_order, kind="point")
a1.fig.suptitle('Golden Boy Winners Wages in Euro per Season')
plt.show()