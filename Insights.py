# *********************** Brian O'Sullivan ***********************
# ********************* Golden Boy Winners ***********************
# *** Insights for Players from the 2021 Season ***
# * https://github.com/brianosullivan241177/UCDPA_BrianOSullivan *

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Fifa_Top_250_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv",
                   usecols=['short_name', 'height_cm', 'overall', 'club_name','potential','age','work_rate','Season','value_eur',
                            'preferred_foot','team_position','skill_ball_control','skill_dribbling','mentality_composure','wage_eur'],
                      index_col="short_name",nrows=250)

print("************************* Top 20 players ****************************")
print(Fifa_Top_250_DF.head(20))
print("************************* Preferred Feet of top 250 - Begin ****************************")
print(Fifa_Top_250_DF.preferred_foot.value_counts())

plt.figure(dpi=125)
sns.countplot('preferred_foot', data=Fifa_Top_250_DF, palette='Blues')
plt.xlabel('Preferred Foot Players')
plt.ylabel('Count')
plt.title('Count of Preferred Foot')
Right, Left = Fifa_Top_250_DF.preferred_foot.value_counts()
print('Left Preferred', Left)
print('Right Preferred', Right)
#plt.show()
print("************************* Preferred Feet of top 250 - End ****************************")
print("***************** Unique Clubs in the top 250 - Begin ************************")
Unique_Clubs_DF = Fifa_Top_250_DF.club_name.unique()[:10] #top 10 unique clubs
print(Unique_Clubs_DF)
print("***************** Unique Clubs in the top 250 - End ************************")
fifa_20_top_attackers = Fifa_Top_250_DF[Fifa_Top_250_DF['team_position'].str.contains('ST|RW|LW|CF|LS|RS')==True]\
    .sort_values(by="overall", ascending=False)

#print(fifa_20_top_attackers.head(20))


print("***************** Merging Data Frames - Begin ************************")
fifa_20_potential = Fifa_Top_250_DF[(Fifa_Top_250_DF.age.astype(int)>=18) & (Fifa_Top_250_DF.age.astype(int)<=40)].groupby(['age'])['potential'].mean()
fifa_20_overall = Fifa_Top_250_DF[(Fifa_Top_250_DF.age.astype(int)>=18) & (Fifa_Top_250_DF.age.astype(int)<=40)].groupby(['age'])['overall'].mean()
fifa_20_summary = pd.concat([fifa_20_potential, fifa_20_overall], axis=1)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(fifa_20_summary)
ax.set_xlabel("Age", fontsize=20)
ax.set_ylabel("Rating", fontsize=20)
ax.set_title("FIFA 20 - Average Rating by Age", fontsize=20)
#plt.show()

print("***************** Merging Data Frames - End ************************")

print("********** Function for player mentality - Begin ****************")
def mental_calc(m):
    if m < 51:
        return "Unpredicatable - Roy Keane like"
    elif m >= 51 and m < 67:
        return "Dependable - Denis Irwin like"
    elif m >= 67:
        return "Cool - Ronaldo like"


for index, row in Fifa_Top_250_DF.iterrows():
    Fifa_Top_250_DF.loc[index, "mentality_composure"] = mental_calc(row["mentality_composure"])

print("********** Function for player mentality - End ****************")

print("**********Dtpye of top 250 - Begin ****************")
print(Fifa_Top_250_DF.dtypes)
print("**********Dtpye of top 250 - End ****************")
print("**********Columns of top 250 - Begin ****************")
print(Fifa_Top_250_DF.columns)
print("**********Columns of top 250 - End ****************")

print("********** Graph for top 250 Mentality - Begin ****************")

plt.figure(figsize=(12,10))
sns.histplot(x="team_position",
             data=Fifa_Top_250_DF,
             hue="mentality_composure",
             multiple="dodge",
             palette="plasma"
            )
#plt.show()
print("********** Graph for top 250 Mentality - End ****************")

print("********** The top subs of top 250 - Begin ****************")

Fifa_20_top_Subs = Fifa_Top_250_DF[Fifa_Top_250_DF['team_position'].str.contains('SUB')==True]\
    .sort_values(by="overall", ascending=False)
print(Fifa_20_top_Subs.head(20))

plt.figure(figsize=(12,10))
sns.histplot(x="team_position",
             data=Fifa_20_top_Subs,
             hue="mentality_composure",
             multiple="dodge",
             palette="plasma"
            )
plt.show()
print("********** The top subs of top 250 - End ****************")