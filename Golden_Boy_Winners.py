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

Golden_Boy_Winners_DF = FifaAll_Players_DF[
    (FifaAll_Players_DF.short_name == 'GB Winner 2010 M. Balotelli')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2011 M. Götze')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2012 Isco')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2013 P. Pogba')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2014 R. Sterling')
]
print(Golden_Boy_Winners_DF)

plot_order = Golden_Boy_Winners_DF.groupby('Season')['short_name'].sum().sort_values(ascending=False).index.values
plot_order2 = Golden_Boy_Winners_DF.sort_values(by=['Season'], inplace=True)
#sns.catplot(data=Golden_Boy_Winners_DF, x='Season',  y='overall',hue='short_name',ci=None, legend_out=False, order=plot_order2,
 #           )
a = sns.catplot(data=Golden_Boy_Winners_DF, x='Season',
                   y='overall', hue='short_name', height=6, aspect=2, order=plot_order2, kind="point")


a = sns.catplot(data=Golden_Boy_Winners_DF, x='Season',
                   y='wage_eur', hue='short_name', height=6, aspect=2, order=plot_order2, kind="point")
plt.show()

