# *********************** Brian O'Sullivan ***********************
# ******************* Players 21 - 22 Season   *******************
# **************** Players from the 2021-2022 Season *************
# * https://github.com/brianosullivan241177/UCDPA_BrianOSullivan *

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['axes.labelsize'] = 15
plt.rcParams['axes.titlesize'] = 15
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12

Fifa_Top_250_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project_Final/Modified/players_21_22.csv",
                   usecols=['short_name', 'height_cm', 'overall','league_name', 'club_name','potential','age','work_rate','Season','value_eur',
                            'preferred_foot','club_position','skill_ball_control','player_positions','goalkeeping_reflexes','goalkeeping_speed','skill_dribbling','mentality_composure','wage_eur'],
                      index_col="short_name",nrows=250)

print("************************* Top 20 players ****************************")
print(Fifa_Top_250_DF.head(20))
print("************************* Preferred Feet of top 250 - Begin ****************************")
print(Fifa_Top_250_DF.preferred_foot.value_counts())

plt.figure(dpi=125)
sns.countplot('preferred_foot', data=Fifa_Top_250_DF, palette='Blues')
plt.xlabel('The players preferred Foot ')
plt.ylabel('Number of players')
plt.title('The preferred foot of the top 250 players in the world')
Right, Left = Fifa_Top_250_DF.preferred_foot.value_counts()
print('Left Preferred', Left)
print('Right Preferred', Right)
#plt.show()
print("************************* Preferred Feet of top 250 - End ****************************")
print("***************** Unique Clubs in the top 250 - Begin ************************")
Unique_Clubs_DF = Fifa_Top_250_DF.club_name.unique()[:10] #top 10 unique clubs
print(Unique_Clubs_DF)
print("***************** Unique Clubs in the top 250 - End ************************")
fifa_20_top_attackers = Fifa_Top_250_DF[Fifa_Top_250_DF['club_position'].str.contains('ST|RW|LW|CF|LS|RS')==True]\
    .sort_values(by="overall", ascending=False)

print("***************** Merging Data Frames - Begin ************************")
fifa_20_potential = Fifa_Top_250_DF[(Fifa_Top_250_DF.age.astype(int)>=18) & (Fifa_Top_250_DF.age.astype(int)<=40)].groupby(['age'])['potential'].mean()
fifa_20_overall = Fifa_Top_250_DF[(Fifa_Top_250_DF.age.astype(int)>=18) & (Fifa_Top_250_DF.age.astype(int)<=40)].groupby(['age'])['overall'].mean()
fifa_20_summary = pd.concat([fifa_20_potential, fifa_20_overall], axis=1)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(fifa_20_summary)
plt.legend(['Avg. Potential', 'Avg. Overall'], loc='upper right')
ax.set_xlabel("Age")
ax.set_ylabel("Avg. Potential Rating - Avg. Overall Rating in % ")
ax.set_title("Player avg. Potential rating v avg. Overall rating by age for the top 250 players")
#plt.show()

print("***************** Merging Data Frames - End ************************")

print("********** Function for player mentality - Begin ****************")
def Mentality_func(m):
    if m < 51:
        return "Unpredicatable"
    elif m >= 51 and m < 67:
        return "Dependable"
    elif m >= 67:
        return "Cool"


for index, row in Fifa_Top_250_DF.iterrows():
    Fifa_Top_250_DF.loc[index, "mentality_composure"] = Mentality_func(row["mentality_composure"])

print("********** Function for player mentality - End ****************")

print("**********Dtpye of top 250 - Begin ****************")
print(Fifa_Top_250_DF.dtypes)
print("**********Dtpye of top 250 - End ****************")
print("**********Columns of top 250 - Begin ****************")
print(Fifa_Top_250_DF.columns)
print("**********Columns of top 250 - End ****************")

print("********** Graph for top 250 Mentality - Begin ****************")

plt.figure(figsize=(12,10))
sns.histplot(x="club_position",
             data=Fifa_Top_250_DF,
             hue="mentality_composure",
             multiple="dodge",
             palette="plasma"
            )
plt.xlabel('Players positions')
plt.ylabel('Number of players')
plt.title('Mentality of the top 250 players by Position')
#plt.show()
print("********** Graph for top 250 Mentality - End ****************")

print("********** The top subs of top 250 - Begin ****************")

Fifa_20_top_Subs = Fifa_Top_250_DF[Fifa_Top_250_DF['club_position'].str.contains('SUB')==True]\
    .sort_values(by="overall", ascending=False)
print(Fifa_20_top_Subs.head(20))

plt.figure(figsize=(12,10))
sns.histplot(x="club_position",
             data=Fifa_20_top_Subs,
             hue="mentality_composure",
             multiple="dodge",
             palette="plasma"
            )
plt.xlabel('Players position')
plt.ylabel('Number of players')
plt.title('Mentality of the top 250 players who are subs')
plt.show()
print("********** The top subs of top 250 - End ****************")
print("********** The top players in the top 250 under 23 - Begin ****************")

Fifa_Top_250_Top_100_DF = Fifa_Top_250_DF.head(100)
fifa_2022_youth_DF = Fifa_Top_250_Top_100_DF[(Fifa_Top_250_Top_100_DF.age<23)]
print(fifa_2022_youth_DF)

plt.figure(figsize=(12,10))
sns.histplot(x="league_name",
             data=fifa_2022_youth_DF,
             hue="league_name",
             multiple="dodge",
             palette="plasma"
            )
plt.xlabel('League')
plt.ylabel('Number of players')
plt.title('The leagues the players under 23 in the top 100 compete in')
plt.show()
print("********** The top players in the top 250 under 23 - End ****************")

print("*************************** Attackers ******************************")
Fifa_20_top_Attack_DF = Fifa_Top_250_DF[Fifa_Top_250_DF['player_positions'].str.contains('ST|LW|RW|LW|CF|CAM|RM|LM')==True].\
    sort_values(by="overall", ascending=False)
print(Fifa_20_top_Attack_DF.head(10))

#Replacing missing values
print("*************************** Replace missing values - Begin ******************************")
Replaced_Fifa_20_top_Attack_DF =  Fifa_20_top_Attack_DF['goalkeeping_speed'].fillna(0,inplace=True)
print("*************************** Replace missing values - End ********************************")

print("************************** Players after filling in gk_positioning ******************************")
print(Fifa_20_top_Attack_DF.head(10))


FifaTop250_Drop_Players_Drop_DF = Fifa_Top_250_DF.drop(['goalkeeping_reflexes'], axis = 1)
print("*************************** Before dropping Goalkeeping reflexes column ****************************")
print(Fifa_Top_250_DF.columns)
print("*************************** After dropping Goalkeeping reflexes column ****************************")
print(FifaTop250_Drop_Players_Drop_DF.columns)

Fifa_Top_250_W_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project_Final/Modified/female_players_21_22.csv",
                   usecols=['short_name', 'height_cm', 'overall','league_name', 'club_name','potential','age','work_rate','Season','value_eur',
                            'preferred_foot','club_position','skill_ball_control','nationality_name','player_positions','goalkeeping_reflexes','goalkeeping_speed','skill_dribbling','mentality_composure','wage_eur'],
                      index_col="short_name",nrows=250)

print("***************** Merging Data Frames - Begin ************************")
fifa_20_potential = Fifa_Top_250_W_DF[(Fifa_Top_250_W_DF.age.astype(int)>=18) & (Fifa_Top_250_W_DF.age.astype(int)<=40)].groupby(['age'])['potential'].mean()
fifa_20_overall = Fifa_Top_250_W_DF[(Fifa_Top_250_W_DF.age.astype(int)>=18) & (Fifa_Top_250_W_DF.age.astype(int)<=40)].groupby(['age'])['overall'].mean()
fifa_20_summary = pd.concat([fifa_20_potential, fifa_20_overall], axis=1)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(fifa_20_summary)
plt.legend(['Avg. Potential', 'Avg. Overall'], loc='upper right')
ax.set_xlabel("Age")
ax.set_ylabel("Avg. Potential Rating - Avg. Overall Rating in % ")
ax.set_title("Womens - Player avg. Potential rating v avg. Overall rating by age for the top 250 womens footballers")
plt.show()

print("************************* Preferred Feet of top 250 - Begin ****************************")
print(Fifa_Top_250_W_DF.preferred_foot.value_counts())

plt.figure(dpi=125)
sns.countplot('preferred_foot', data=Fifa_Top_250_W_DF, palette='Blues')
plt.xlabel('The players preferred Foot ')
plt.ylabel('Number of players')
plt.title('Womens - preferred foot of the top 250 players in the world')
Right, Left = Fifa_Top_250_W_DF.preferred_foot.value_counts()
print('Left Preferred', Left)
print('Right Preferred', Right)
plt.show()
