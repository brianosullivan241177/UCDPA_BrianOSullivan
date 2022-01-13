import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

import np as numpy


Fifa_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv",
                   usecols=['short_name', 'height_cm', 'overall', 'potential','age','work_rate','Season','league_name','club_name'])


print("************************* Relegated **********************************")
English_PL_Relegated_20142015_DF = Fifa_DF[(Fifa_DF.league_name == 'English Premier League')
                                        &(Fifa_DF.Season == '2014-2015')
                                           &((Fifa_DF.club_name == 'Hull City')
                                                                                           | (Fifa_DF.club_name == 'Burnley')
                                                                                           | (Fifa_DF.club_name == 'Queens Park Rangers'))] #Premier League players
print(English_PL_Relegated_20142015_DF) #Premier League relegated players - top records

print("************************* Relegated - End **********************************")
print("************************* Escaped Relegation **********************************")
English_PL_Escaped_Relegation_20142015_DF=Fifa_DF[(Fifa_DF.league_name == 'English Premier League')
                                                &(Fifa_DF.Season == '2014-2015')
                                                  & ((Fifa_DF.club_name == 'Newcastle United')
                                                                                                  | (Fifa_DF.club_name == 'Sunderland')
                                                                                                  | (Fifa_DF.club_name == 'Aston Villa'))] #Premier League players
print(English_PL_Escaped_Relegation_20142015_DF) #Premier League escaped relegatio players - top records

print("************************* Escaped Relegation - End **********************************")
print("************************* Combined Dataframes - Begin **********************************")
Combined_DF = [English_PL_Relegated_20142015_DF, English_PL_Escaped_Relegation_20142015_DF]
print(Combined_DF)
print("************************* Combined Dataframes - End **********************************")
print("************************* Combined Dataframes - Axis - Begin **********************************")
Axis_DF = pd.concat([English_PL_Relegated_20142015_DF,English_PL_Escaped_Relegation_20142015_DF],axis=1)
print(Axis_DF)

#Combined_DF.plot(kind='scatter',x='overall',y='age',color='red')
#plt.show()

#Replaced_Axis_DF = Axis_DF['short_name'] = Axis_DF['age'].fillna(0,inplace=True)
#print(Replaced_Axis_DF)

#fifa_20_potential = Replaced_Axis_DF[(Replaced_Axis_DF.age.astype(int)>=18) & (Replaced_Axis_DF.age.astype(int)<=40)].groupby(['age'])['potential'].mean()
#fifa_20_overall = Replaced_Axis_DF[(Replaced_Axis_DF.age.astype(int)>=18) & (Replaced_Axis_DF.age.astype(int)<=40)].groupby(['age'])['overall'].mean()
#fifa_20_summary = pd.concat([fifa_20_potential, fifa_20_overall], axis=1)
#fig, ax = plt.subplots(figsize=(16, 8))
#ax.plot(fifa_20_summary)
#ax.set_xlabel("Age", fontsize=20)
#ax.set_ylabel("Rating", fontsize=20)
#ax.set_title("FIFA 20 - Average Rating by Age", fontsize=20)
#plt.show()

plt.figure(figsize=(12,10))
sns.histplot(x="Season",
             data=Combined_DF,
             hue="club_name",
             multiple="dodge",
             palette="plasma"
            )
plt.show()
