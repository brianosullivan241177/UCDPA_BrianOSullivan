# *********************** Brian O'Sullivan ***********************
# ********************* Golden Boy Winners ***********************
# ********************** Irish Fifa records **********************
# * https://github.com/brianosullivan241177/UCDPA_BrianOSullivan *
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project_Final/Modified/FIFAAllplayersM.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality_name','potential','international_reputation',])
print(FifaAll_Players_DF.head()) #top records
print(FifaAll_Players_DF.dtypes) #dataframe data tyoes

# Irish players in the premier league - wages
print("******************* Irish players in the premier league - wages - Begin ********************")
Irish_Players_PL_DF = FifaAll_Players_DF[(FifaAll_Players_DF.nationality_name == 'Republic of Ireland') &
                                      (FifaAll_Players_DF.league_name == 'English Premier League')]
print(Irish_Players_PL_DF)
print("******************* Irish players in the premier league - wages - End   ********************")

All_Irish_Players_DF = FifaAll_Players_DF[(FifaAll_Players_DF.nationality_name == 'Republic of Ireland')]

plt.figure(dpi=125)
sns.countplot('international_reputation',data=Irish_Players_PL_DF.head(100),palette='Blues')
plt.xlabel('International Reputation')
plt.ylabel('Number of Players')
plt.title('International Reputation of the top 100 Irish Players')
plt.show()

Irish_PL_wages = Irish_Players_PL_DF.groupby('Season')['wage_eur'].agg(['mean', 'count'])
Irish_PL_wages = Irish_PL_wages.sort_values(by = 'Season', ascending = True)

fig = px.bar(Irish_PL_wages[0:10], x= Irish_PL_wages.index[0:10], y='mean') # will show up to 10 seasons
fig.update_layout(title_text='Mean wages - Irish Players in the Premier League')
fig.update_xaxes(title_text="<b> Season </b>")
fig.update_yaxes(title_text="<b> Mean Wages </b>")
fig.show()

# Irish players outside the premier league - wages
Irish_Players_Excl_PL_DF = FifaAll_Players_DF[(FifaAll_Players_DF.nationality_name == 'Republic of Ireland') &
                                      (FifaAll_Players_DF.league_name != 'English Premier League')]

print(Irish_Players_Excl_PL_DF)
Irish_Excl_PL_wages = Irish_Players_Excl_PL_DF.groupby('Season')['wage_eur'].agg(['mean', 'count'])
Irish_Excl_PL_wages = Irish_Excl_PL_wages.sort_values(by = 'Season', ascending = True)

fig1 = px.bar(Irish_Excl_PL_wages[0:10], x= Irish_Excl_PL_wages.index[0:10], y='mean') # will show up to 10 seasons
fig1.update_layout(title_text='Mean wages - Irish Players outside the Premier League')
fig1.update_xaxes(title_text="<b> Season </b>")
fig1.update_yaxes(title_text="<b> Mean Wages </b>")
fig1.show()


Captains_DF = FifaAll_Players_DF[(FifaAll_Players_DF.short_name == 'S. Coleman')
                                |(FifaAll_Players_DF.short_name == 'G. Bale')
                                |(FifaAll_Players_DF.sofifa_id == 216267)
                                |(FifaAll_Players_DF.sofifa_id == 202126) #more than one H. Kane

]
print(Captains_DF)

#Coleman_Season_Grouped = Captains_DF.sort_values(['wage_eur'],ascending=False).groupby('Season').head(3)
#print(Coleman_Season_Grouped)


#Seamus_wages = Coleman_Season_Grouped.groupby('Season')['wage_eur'].agg(['mean', 'count'])
#Seamus_wages = Seamus_wages.sort_values(by = 'Season', ascending = True)
#fig2 = px.bar(Seamus_wages[0:10], x= Seamus_wages.index[0:10], y='mean') # will show up to 10 seasons
#fig2.update_layout(title_text='Mean wages - Seamus Coleman')
#fig2.update_xaxes(title_text="<b> Season </b>")
#fig2.update_yaxes(title_text="<b> Mean Wages </b>")
#fig2.show()

plot_order = Captains_DF.sort_values(by=['Season'], inplace=True)
Captains_DF.rename(columns = {'overall':'Overall Rating in %', 'wage_eur':'Wages paid in Euro',
                                     'short_name':'Player_name'}, inplace = True)

a = sns.catplot(data=Captains_DF, x='Season',
                   y='Overall Rating in %', hue='Player_name', height=6, aspect=2, kind="point", order=plot_order)
a.fig.suptitle('Irish captains overall rating in % compared to neighbour countries')
plt.show()

import pandas as pd
Players_21_22_DF= pd.read_csv('/users/brian/documents/FIFA_Project_Final/Modified/players_21_22.csv')

def findminmax(col):
    top = Players_21_22_DF[col].idxmax()
    top_df = pd.DataFrame(Players_21_22_DF.loc[0])
    bottom = Players_21_22_DF[col].idxmin()
    bottom_df = pd.DataFrame(Players_21_22_DF.loc[1])
    info_df = pd.concat([top_df, bottom_df], axis=1)
    return info_df


findminmax('wage_eur')

def Country(x):
    def findminmax(col):
        work = Players_21_22_DF[col].idxmax()
        work_df = pd.DataFrame(Players_21_22_DF.loc[work])
        return work_df
    return Players_21_22_DF[Players_21_22_DF['nationality_name'] == x ][['goalkeeping_handling', 'short_name']].sort_values\
        (by=['goalkeeping_handling'],ascending=False)
findminmax('goalkeeping_handling')
Country1 = Country("Republic of Ireland")
print(Country1)
goalkeeper = Country1.iloc[0][1]
print("The goalkeeper is :", goalkeeper)


print("*********************************************")
Players_21_22_DF['fullback_mean']=Players_21_22_DF['defending_sliding_tackle'] \
                                  + Players_21_22_DF['passing'] + Players_21_22_DF['defending'] + \
                                  Players_21_22_DF['skill_long_passing'] + Players_21_22_DF['power_strength']
Players_21_22_DF


def Country(x):
    def findminmax(col):
        work = Players_21_22_DF[col].idxmax()
        work_df = pd.DataFrame(Players_21_22_DF.loc[work])
        return work_df
    return Players_21_22_DF[Players_21_22_DF['nationality_name'] == x ][['fullback_mean', 'short_name']]\
        .sort_values(by=['fullback_mean'],ascending=False)

Country1 = Country("Republic of Ireland")
print(Country1)
fullback1=Country1.iloc[0][1]
print("The fullback one is :", fullback1)
fullback2=Country1.iloc[1][1]
print("The fullback two is :", fullback2)


print("*********************************************")




Players_21_22_DF.drop(Players_21_22_DF[Players_21_22_DF['short_name']==fullback1].index, inplace = True)
Players_21_22_DF.drop(Players_21_22_DF[Players_21_22_DF['short_name']==fullback2].index, inplace = True)


Players_21_22_DF['centreback_mean']=Players_21_22_DF['movement_agility'] + Players_21_22_DF['pace']+ Players_21_22_DF['movement_reactions'] \
                         + Players_21_22_DF['defending_sliding_tackle'] + Players_21_22_DF['defending']
Players_21_22_DF

def Country(x):
    def findminmax(col):
        work = Players_21_22_DF[col].idxmax()
        work_df = pd.DataFrame(Players_21_22_DF.loc[work])
        return work_df
    return Players_21_22_DF[Players_21_22_DF['nationality_name'] == x ][['centreback_mean', 'short_name']].sort_values(by=['centreback_mean'],ascending=False)
findminmax('centreback_mean')
Country1 = Country("Republic of Ireland")
print(Country1)
centreback1=Country1.iloc[0][1]
centreback2=Country1.iloc[1][1]
print("The first wing back is :", centreback1)
print("The second wing back is :", centreback2)


Players_21_22_DF.drop(Players_21_22_DF[Players_21_22_DF['short_name']=='centreback_mean'].index, inplace = True)

Players_21_22_DF['centremidfielder_mean']=Players_21_22_DF['dribbling'] + Players_21_22_DF['passing'] + Players_21_22_DF['pace'] + Players_21_22_DF['movement_agility']+ Players_21_22_DF['movement_reactions'] + Players_21_22_DF['movement_balance'] + Players_21_22_DF['attacking_short_passing']+ Players_21_22_DF['attacking_heading_accuracy']
Players_21_22_DF





def Country(x):
    def findminmax(col):
        work = Players_21_22_DF[col].idxmax()
        work_df = pd.DataFrame(Players_21_22_DF.loc[work])
        return work_df
    return Players_21_22_DF[Players_21_22_DF['nationality_name'] == x ][['centremidfielder_mean', 'short_name']].sort_values(by=['centremidfielder_mean'],ascending=False)
findminmax('centremidfielder_mean')
Country1 = Country("Republic of Ireland")
print(Country1)
centremidfielder1=Country1.iloc[0][1]
print("The centremidfielder one is :", centremidfielder1)
centremidfielder2=Country1.iloc[1][1]
print("The centremidfielder two is :", centremidfielder2)
centremidfielder3=Country1.iloc[2][1]
print("The centremidfielder three is :", centremidfielder3)
centremidfielder4=Country1.iloc[3][1]
print("The centremidfielder four is :", centremidfielder4)

Players_21_22_DF.drop(Players_21_22_DF[Players_21_22_DF['short_name']==centremidfielder1].index, inplace = True)
Players_21_22_DF.drop(Players_21_22_DF[Players_21_22_DF['short_name']==centremidfielder2].index, inplace = True)
Players_21_22_DF.drop(Players_21_22_DF[Players_21_22_DF['short_name']==centremidfielder3].index, inplace = True)

Players_21_22_DF['attackingmidfielder_mean']=Players_21_22_DF['attacking_finishing'] + Players_21_22_DF['passing'] + Players_21_22_DF['pace'] + Players_21_22_DF['attacking_heading_accuracy']+ Players_21_22_DF['attacking_short_passing'] + Players_21_22_DF['attacking_volleys'] + Players_21_22_DF['skill_curve']
Players_21_22_DF

def Country(x):
    def findminmax(col):
        work = Players_21_22_DF[col].idxmax()
        work_df = pd.DataFrame(Players_21_22_DF.loc[work])
        return work_df
    return Players_21_22_DF[Players_21_22_DF['nationality_name'] == x ][['attackingmidfielder_mean', 'short_name']].sort_values(by=['attackingmidfielder_mean'],ascending=False)
# findminmax('attackingmidfielder_mean')
Country1 = Country("Republic of Ireland")
print(Country1)
attackingmidfielder1=Country1.iloc[0][1]
print("The attackingmidfielder one is :", attackingmidfielder1)
attackingmidfielder2=Country1.iloc[1][1]
print("The attackingmidfielder two is :", attackingmidfielder2)


Players_21_22_DF.drop(Players_21_22_DF[Players_21_22_DF['short_name']==attackingmidfielder1].index, inplace = True)
Players_21_22_DF.drop(Players_21_22_DF[Players_21_22_DF['short_name']==attackingmidfielder2].index, inplace = True)

Players_21_22_DF['striker_mean']=Players_21_22_DF['attacking_finishing'] + Players_21_22_DF['attacking_heading_accuracy'] + Players_21_22_DF['attacking_crossing'] + Players_21_22_DF['pace'] + Players_21_22_DF['skill_curve'] + Players_21_22_DF['skill_fk_accuracy'] + Players_21_22_DF['movement_balance']
Players_21_22_DF

def Country(x):

    return Players_21_22_DF[Players_21_22_DF['nationality_name'] == x ][['striker_mean', 'short_name']].sort_values(by=['striker_mean'],ascending=False)

Country1 = Country("Republic of Ireland")
print(Country1)
striker=Country1.iloc[0][1]
print("The stricker is :", striker)

Players_21_22_DF.drop(Players_21_22_DF[Players_21_22_DF['short_name']==striker].index, inplace = True)

print("The team is ",
      goalkeeper, fullback1, fullback2,centreback1,centreback2,centremidfielder1, centremidfielder2, centremidfielder3, attackingmidfielder1,
      attackingmidfielder2, striker)

print("Goalkeeper is ", goalkeeper)
print("First Full back is ", fullback1)
print("Second Full back is ", fullback2)
print("First Centre back is ", centreback1)
print("Second Centre back is ", centreback2)
print("Central Midfield is ",centremidfielder1)
print("Central Midfield  is ",centremidfielder2)
print("Central Midfield  is ",centremidfielder3)
print("Attacking Midfield one is ",attackingmidfielder1)
print("Attacking Midfield one is ",attackingmidfielder2)
print("Striker ",striker)


from mplsoccer import Pitch
import matplotlib.pyplot as plt
pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
fig, ax = pitch.draw()
a.fig.suptitle('Golden Boy Winners Overall ratings in % per Season')
plt.text(1,40,goalkeeper)
plt.text(15,4, fullback1)
plt.text(15,79,fullback2)
plt.text(20,20,centreback1)
plt.text(20,60,centreback2)
plt.text(50,20,centremidfielder1)
plt.text(50,40,centremidfielder2)
plt.text(50,60,centremidfielder3)
plt.text(80,50,attackingmidfielder1)
plt.text(80,30,attackingmidfielder2)
plt.text(100,40,striker)
plt.title("Best Irish Team according to stats for the 2020-2021 season")
plt.show()


