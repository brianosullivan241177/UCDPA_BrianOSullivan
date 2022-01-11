import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/Allplayers.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential'], index_col=[0])
print(FifaAll_Players_DF.head()) #top records
print(FifaAll_Players_DF.dtypes) #dataframe data tyoes

# Irish players in the premier league - wages
print("******************* Irish players in the premier league - wages - Begin ********************")
Irish_Players_PL_DF = FifaAll_Players_DF[(FifaAll_Players_DF.nationality == 'Republic of Ireland') &
                                      (FifaAll_Players_DF.league_name == 'English Premier League')]
print(Irish_Players_PL_DF)
print("******************* Irish players in the premier league - wages - End   ********************")
Irish_PL_wages = Irish_Players_PL_DF.groupby('Season')['wage_eur'].agg(['mean', 'count'])
Irish_PL_wages = Irish_PL_wages.sort_values(by = 'Season', ascending = True)

fig = px.bar(Irish_PL_wages[0:10], x= Irish_PL_wages.index[0:10], y='mean') # will show up to 10 seasons
fig.update_layout(title_text='Mean wages - Irish Players in the Premier League')
fig.update_xaxes(title_text="<b> Season </b>")
#fig.show()

# Irish players outside the premier league - wages
Irish_Players_Excl_PL_DF = FifaAll_Players_DF[(FifaAll_Players_DF.nationality == 'Republic of Ireland') &
                                      (FifaAll_Players_DF.league_name != 'English Premier League')]

print(Irish_Players_Excl_PL_DF)
Irish_Excl_PL_wages = Irish_Players_Excl_PL_DF.groupby('Season')['wage_eur'].agg(['mean', 'count'])
Irish_Excl_PL_wages = Irish_Excl_PL_wages.sort_values(by = 'Season', ascending = True)

fig1 = px.bar(Irish_Excl_PL_wages[0:10], x= Irish_Excl_PL_wages.index[0:10], y='mean') # will show up to 10 seasons
fig1.update_layout(title_text='Mean wages - Irish Players outside the Premier League')
fig1.update_xaxes(title_text="<b> Season </b>")
#fig1.show()


Coleman_DF = FifaAll_Players_DF[(FifaAll_Players_DF.short_name == 'S. Coleman')
                                |(FifaAll_Players_DF.short_name == 'L. Messi')
                                |(FifaAll_Players_DF.short_name == 'Cristiano Ronaldo')  ]
print(Coleman_DF)

Coleman_Season_Grouped = Coleman_DF.sort_values(['wage_eur'],ascending=False).groupby('Season').head(3)
print(Coleman_Season_Grouped)


Seamus_wages = Coleman_Season_Grouped.groupby('Season')['wage_eur'].agg(['mean', 'count'])
Seamus_wages = Seamus_wages.sort_values(by = 'Season', ascending = True)
fig2 = px.bar(Seamus_wages[0:10], x= Seamus_wages.index[0:10], y='mean') # will show up to 10 seasons
fig2.update_layout(title_text='Mean wages - Seamus Coleman')
fig2.update_xaxes(title_text="<b> Season </b>")
fig2.show()


a = sns.catplot(data=Coleman_DF, x='Season',
                   y='overall', hue='short_name', height=6, aspect=2, kind="point")
plt.show()
#d = grouped_data.get_group(("Real Madrid", 20801))
#sns.lineplot(x=Seamus_wages["Season"], y=Seamus_wages['overall'])
#plt.xticks(d.year)
#plt.title("Ronaldo's pace over the years when he was in Real Madrid")

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import plotly.graph_objects as go
# Module for creating blocks
from plotly.subplots import make_subplots
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
print("Setup Complete")
dataset= pd.read_csv('/users/brian/documents/FIFA_Project/Modified/players_20_21.csv')

def find_min_max_in(col):
    top = dataset[col].idxmax()
    top_df = pd.DataFrame(dataset.loc[0])

    bottom = dataset[col].idxmin()
    bottom_df = pd.DataFrame(dataset.loc[1])

    info_df = pd.concat([top_df, bottom_df], axis=1)
    return info_df


find_min_max_in('wage_eur')

def Country(x):
    def find_min_max_in(col):
        work = dataset[col].idxmax()
        work_df = pd.DataFrame(dataset.loc[work])
        return work_df
    return dataset[dataset['nationality'] == x ][['goalkeeping_handling', 'short_name']].sort_values(by=['goalkeeping_handling'],ascending=False)
find_min_max_in('goalkeeping_handling')
Country1 = Country("Republic of Ireland")
print(Country1)
goalkeeper = Country1.iloc[0][1]
print("The goalkeeper is :", goalkeeper)


dataset['wingback_mean']=dataset['movement_agility'] + dataset['pace']+ dataset['movement_reactions'] + dataset['passing'] + dataset['defending_sliding_tackle'] + dataset['defending']
dataset

def Country(x):
    def find_min_max_in(col):
        work = dataset[col].idxmax()
        work_df = pd.DataFrame(dataset.loc[work])
        return work_df
    return dataset[dataset['nationality'] == x ][['wingback_mean', 'short_name']].sort_values(by=['wingback_mean'],ascending=False)
find_min_max_in('wingback_mean')
Country1 = Country("Republic of Ireland")
print(Country1)
centreback=Country1.iloc[0][1]
centreback1=Country1.iloc[1][1]
print("The first wing back is :", centreback)
print("The second wing back is :", centreback1)

# dataset=dataset.drop(dataset.index[[822]])
dataset.drop(dataset[dataset['short_name']==centreback].index, inplace = True)

dataset['centremidfielder_mean']=dataset['dribbling'] + dataset['passing'] + dataset['pace'] + dataset['movement_agility']+ dataset['movement_reactions'] + dataset['movement_balance'] + dataset['attacking_short_passing']+ dataset['attacking_heading_accuracy']
dataset





def Country(x):
    def find_min_max_in(col):
        work = dataset[col].idxmax()
        work_df = pd.DataFrame(dataset.loc[work])
        return work_df
    return dataset[dataset['nationality'] == x ][['centremidfielder_mean', 'short_name']].sort_values(by=['centremidfielder_mean'],ascending=False)
find_min_max_in('centremidfielder_mean')
Country1 = Country("Republic of Ireland")
print(Country1)
centremidfielder1=Country1.iloc[0][1]
print("The centremidfielder one is :", centremidfielder1)
centremidfielder2=Country1.iloc[1][1]
print("The centremidfielder two is :", centremidfielder2)
centremidfielder3=Country1.iloc[2][1]
print("The centremidfielder three is :", centremidfielder3)
# dataset=dataset.drop(dataset.index[[152]])
# dataset=dataset.drop(dataset.index[[891]])
# dataset=dataset.drop(dataset.index[[825]])
dataset.drop(dataset[dataset['short_name']==centremidfielder1].index, inplace = True)
dataset.drop(dataset[dataset['short_name']==centremidfielder2].index, inplace = True)
dataset.drop(dataset[dataset['short_name']==centremidfielder3].index, inplace = True)

dataset['attackingmidfielder_mean']=dataset['attacking_finishing'] + dataset['passing'] + dataset['pace'] + dataset['attacking_heading_accuracy']+ dataset['attacking_short_passing'] + dataset['attacking_volleys'] + dataset['skill_curve']
dataset

def Country(x):
    def find_min_max_in(col):
        work = dataset[col].idxmax()
        work_df = pd.DataFrame(dataset.loc[work])
        return work_df
    return dataset[dataset['nationality'] == x ][['attackingmidfielder_mean', 'short_name']].sort_values(by=['attackingmidfielder_mean'],ascending=False)
# find_min_max_in('attackingmidfielder_mean')
Country1 = Country("Republic of Ireland")
print(Country1)
attackingmidfielder1=Country1.iloc[0][1]
print("The attackingmidfielder one is :", attackingmidfielder1)
attackingmidfielder2=Country1.iloc[1][1]
print("The attackingmidfielder two is :", attackingmidfielder2)
# dataset=dataset.drop(dataset.index[[2042]])
# print(dataset.index[dataset['short_name']].tolist())
# dataset=dataset.drop(dataset.index[[876]])
dataset.drop(dataset[dataset['short_name']==attackingmidfielder1].index, inplace = True)
dataset.drop(dataset[dataset['short_name']==attackingmidfielder2].index, inplace = True)

dataset['stricker_mean']=dataset['attacking_finishing'] + dataset['attacking_heading_accuracy'] + dataset['attacking_crossing'] + dataset['pace'] + dataset['skill_curve'] + dataset['skill_fk_accuracy'] + dataset['movement_balance']
dataset

def Country(x):
#     def find_min_max_in(col):
#         work = dataset[col].idxmax()
#         work_df = pd.DataFrame(dataset.loc[work])
#         return work_df
    return dataset[dataset['nationality'] == x ][['stricker_mean', 'short_name']].sort_values(by=['stricker_mean'],ascending=False)
# find_min_max_in('stricker_mean')
Country1 = Country("Republic of Ireland")
print(Country1)
stricker=Country1.iloc[0][1]
print("The stricker is :", stricker)
# dataset=dataset.drop(dataset.index[[822]])
dataset.drop(dataset[dataset['short_name']==stricker].index, inplace = True)

dataset['fullback_mean']=dataset['defending_sliding_tackle'] + dataset['passing'] + dataset['defending'] + dataset['skill_long_passing'] + dataset['power_strength']
dataset


def Country(x):
    def find_min_max_in(col):
        work = dataset[col].idxmax()
        work_df = pd.DataFrame(dataset.loc[work])
        return work_df
    return dataset[dataset['nationality'] == x ][['fullback_mean', 'short_name']].sort_values(by=['fullback_mean'],ascending=False)
# find_min_max_in('fullback_mean')
Country1 = Country("Republic of Ireland")
print(Country1)
fullback1=Country1.iloc[0][1]
print("The fullback one is :", fullback1)
fullback2=Country1.iloc[1][1]
print("The fullback two is :", fullback2)


# dataset=dataset.drop(dataset.index[[2054]])
# dataset=dataset.drop(dataset.index[[890]])
# dataset=dataset.drop(dataset.index[[825]])
dataset.drop(dataset[dataset['short_name']==fullback1].index, inplace = True)
dataset.drop(dataset[dataset['short_name']==fullback2].index, inplace = True)


print("The team is ",
      goalkeeper, fullback1, fullback2, centremidfielder1, centremidfielder2, centremidfielder3, attackingmidfielder1,
      attackingmidfielder2, centreback, stricker)

