# *********************** Brian O'Sullivan ***********************
# ***************** Ireland compared to Croatia ******************
# * https://github.com/brianosullivan241177/UCDPA_BrianOSullivan *

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['axes.labelsize'] = 15
plt.rcParams['axes.titlesize'] = 15
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12

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

Irish_Nationality_DF.rename(columns = {'overall':'Overall Rating in %', 'wage_eur':'Wages paid in Euro',
                                     'long_name':'Player Name'}, inplace = True)
plot_order = Irish_Nationality_DF.sort_values(by=['Season'], inplace=True)
#
a = sns.catplot(data=Irish_Nationality_DF, x='Season',
                   y='Overall Rating in %', hue='Player Name', height=6, aspect=2, order=plot_order, kind="point")
plt.subplots_adjust(top=0.9)
plt.title('Irish players with an Overall rating  >= 78 in % by Season')
#a = sns.catplot(data=Irish_Nationality_DF, x='Season',
                #   y='Wages paid in Euro', hue='Player Name', height=6, aspect=2, order=plot_order, kind="point")
#plt.xlabel('Season')
#plt.ylabel('Wages in Euro')
#plt.title('Irish players Wages by Season')
#plt.show()

top_irish_df = Irish_Nationality_DF.head(5)
print(top_irish_df)



Croatia_Nationality_DF = FifaAll_Players_DF[
    (FifaAll_Players_DF.nationality_name == 'Croatia')
   # & (FifaAll_Players_DF.league_name == 'English Premier League')
    & (FifaAll_Players_DF.overall >= 78)
]
print(Croatia_Nationality_DF)
#
Croatia_Nationality_DF.rename(columns = {'overall':'Overall Rating in %', 'wage_eur':'Wages paid in Euro',
                                     'long_name':'Player Name'}, inplace = True)
plot_order = Croatia_Nationality_DF.sort_values(by=['Season'], inplace=True)
#
a = sns.catplot(data=Croatia_Nationality_DF, x='Season',
                   y='Overall Rating in %', hue='Player Name', height=6, aspect=2, order=plot_order, kind="point")
plt.subplots_adjust(top=0.9)
plt.title('Croatian players with an Overall rating  >= 78 in % by Season')
#a = sns.catplot(data=Croatia_Nationality_DF, x='Season',
 #                  y='Wages paid in Euro', hue='Player Name', height=6, aspect=2, order=plot_order, kind="point")
plt.show()

top_Croatia_df = Croatia_Nationality_DF.head(5)
print(top_Croatia_df)

plt.figure(dpi=125)
sns.distplot(a=Irish_Nationality_DF['Overall Rating in %'],kde=False,bins=20)
plt.axvline(x=np.mean(Irish_Nationality_DF['Overall Rating in %']),c='green',label='Mean Overall Rating of All Players')
plt.legend()
plt.xlabel('Overall Rating in %')
plt.ylabel('Number of Players')
plt.title('Ireland - Distribution of Overall Player Rating in %')
plt.show()



plt.figure(dpi=125)
sns.distplot(a=Croatia_Nationality_DF['Overall Rating in %'],kde=False,bins=20)
plt.axvline(x=np.mean(Croatia_Nationality_DF['Overall Rating in %']),c='green',label='Mean Overall Rating of All Players')
plt.legend()
plt.xlabel('Overall Rating in %')
plt.ylabel('Number of Players')
plt.title('Croatia - Distribution of Overall Player Rating in %')
plt.show()