
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

Fifa_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv",
                   usecols=['short_name', 'height_cm',
                            'overall', 'potential','age','work_rate','Season','league_name','club_name','mentality_composure'
                            ,'shooting','pace','passing','dribbling','defending','physic','league_name'])




def mental_calc(m):
    if m < 51:
        return "Unstable and Turbulent"
    elif m >= 51 and m < 67:
        return "Stable"
    elif m >= 67:
        return "Calm and Composed"

    print("Mentality")

    for index, row in English_Bottom_6_DF.iterrows():
        English_Bottom_6_DF.loc[index, "mentality_composure"] = mental_calc(row["mentality_composure"])

English_Bottom_6_DF =Fifa_DF[(Fifa_DF.league_name == 'English Premier League')
                                                &(Fifa_DF.Season == '2014-2015')
                                                  & (
                                                    (Fifa_DF.club_name == 'Newcastle United')
                                                    | (Fifa_DF.club_name == 'Sunderland')
                                                    | (Fifa_DF.club_name == 'Aston Villa')
                                                    | (Fifa_DF.club_name == 'Hull City')
                                                    | (Fifa_DF.club_name == 'Burnley')
                                                    | (Fifa_DF.club_name == 'Queens Park Rangers'))]


plt.figure(figsize=(12,10))
sns.histplot(x="club_name",
             data=English_Bottom_6_DF,
             hue="work_rate",
             multiple="dodge",
             palette="plasma"
            )
#plt.show()

plt.figure(dpi=125)
sns.displot(a=English_Bottom_6_DF['age'],kde=False,bins=20)
plt.axvline(x=np.mean(English_Bottom_6_DF['age']),c='green',label='Mean Age of All Players in bottom 6')
plt.legend()
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Age')
#plt.show()

Test_DF = English_Bottom_6_DF[['short_name','club_name','shooting','pace','passing',''
                                                                                    'dribbling','defending','physic','league_name']].\
    groupby('club_name').mean().sort_values('shooting',ascending=False).mean(axis=1)

print(Test_DF)

plt.figure(dpi=125)
sns.displot(a=Test_DF,kde=False,bins=20)
plt.axvline(x=np.mean(Test_DF),c='green',label='Mean Age of All Players in bottom 6')
plt.legend()
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Age')

plt.show()