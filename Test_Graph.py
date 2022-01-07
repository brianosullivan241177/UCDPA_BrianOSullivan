import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.graph_objects as go
#%matplotlib inline


Fifa_Top_50_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv",
                   usecols=['short_name', 'height_cm', 'overall', 'club_name','potential','age','work_rate','Season','value_eur',
                            'preferred_foot','team_position','skill_ball_control','skill_dribbling','mentality_composure'],
                      index_col="short_name",nrows=50)

print("************************* Top 20 players ****************************")
print(Fifa_Top_50_DF.head(20))
print(Fifa_Top_50_DF.columns)

sns.relplot(x='overall', y='value_eur', hue='age', palette='viridis', size="age", sizes=(15, 200), aspect=2, data=Fifa_Top_50_DF)
plt.title('Overall Rating vs Value in Euros', fontsize = 20)
plt.xlabel('Overall Rating')
plt.ylabel('Value in Euros')
#plt.show()

print(Fifa_Top_50_DF.preferred_foot.value_counts())

plt.figure(dpi=125)
sns.countplot('preferred_foot', data=Fifa_Top_50_DF, palette='Blues')
plt.xlabel('Preferred Foot Players')
plt.ylabel('Count')
plt.title('Count of Preferred Foot')
Right, Left = Fifa_Top_50_DF.preferred_foot.value_counts()
print('Left Preferred', Left)
print('Right Preferred', Right)
#plt.show()

foot = ['Left', 'Right']
data = Fifa_Top_50_DF.query('preferred_foot in @foot')
fig = px.pie(data, names='preferred_foot',
             color_discrete_sequence=px.colors.sequential.Bluered,
             title='Overall Preferred foot percentages')
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  font=dict(size=12, color='#000000'))
#fig.show()
Unique_Clubs_DF = Fifa_Top_50_DF.club_name.unique()[:20]
print(Unique_Clubs_DF)

fifa_20_top_attackers = Fifa_Top_50_DF[Fifa_Top_50_DF['team_position'].str.contains('ST|RW|LW|CF|LS|RS')==True]\
    .sort_values(by="overall", ascending=False)
print(fifa_20_top_attackers.head(20))

sns.lmplot(x='skill_ball_control', y='skill_dribbling', data=Fifa_Top_50_DF[:1000], col='preferred_foot')
#plt.show()


fifa_20_potential = Fifa_Top_50_DF[(Fifa_Top_50_DF.age.astype(int)>=18) & (Fifa_Top_50_DF.age.astype(int)<=40)].groupby(['age'])['potential'].mean()
fifa_20_overall = Fifa_Top_50_DF[(Fifa_Top_50_DF.age.astype(int)>=18) & (Fifa_Top_50_DF.age.astype(int)<=40)].groupby(['age'])['overall'].mean()
fifa_20_summary = pd.concat([fifa_20_potential, fifa_20_overall], axis=1)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(fifa_20_summary)
ax.set_xlabel("Age", fontsize=20)
ax.set_ylabel("Rating", fontsize=20)
ax.set_title("FIFA 20 - Average Rating by Age", fontsize=20)
#plt.show()


def mental_calc(m):
    if m < 51:
        return "Unstable and Turbulent"
    elif m >= 51 and m < 67:
        return "Stable"
    elif m >= 67:
        return "Calm and Composed"

print("Mentality")

for index, row in Fifa_Top_50_DF.iterrows():
    Fifa_Top_50_DF.loc[index, "mentality_composure"] = mental_calc(row["mentality_composure"])

Fifa_Top_50_DF.head(5)

plt.figure(figsize=(12,10))
sns.histplot(x="club_name",
             data=Fifa_Top_50_DF,
             hue="mentality_composure",
             multiple="dodge",
             palette="plasma"
            )
plt.show()