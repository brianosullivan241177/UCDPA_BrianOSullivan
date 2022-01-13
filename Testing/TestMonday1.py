import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/Allplayers.csv')

#data1 = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/players_19_20.csv')

Season19_20_DF = data[(data.Season == '2019-2020')]
Season20_21_DF = data[(data.Season == '2020-2021')]
top_15 = Season19_20_DF[['short_name','club_name','overall','Season']]\
    .groupby('club_name').mean().sort_values('overall',ascending=False).mean(axis=1)
print(top_15.head())

top_15b = Season20_21_DF[['short_name','club_name','overall','Season']]\
    .groupby('club_name').mean().sort_values('overall',ascending=False).mean(axis=1)
print(top_15b.head())

Brian_DF = pd.concat([top_15, top_15b], axis=1)

#a = sns.catplot(data=Brian_DF, x='Season',
                  # y='overall', hue='short_name', height=6, aspect=2, kind="point")


df15 = pd.read_csv("/users/brian/documents/FIFA_Project/Modified/players_14_15.csv")
df16 = pd.read_csv("/users/brian/documents/FIFA_Project/Modified/players_15_16.csv")

df18_top = df18[((df18["age"]<=25) & (df18["age"]>=21))].sort_values(by = "overall",ascending = False).head(200)
df15_prospects = df15.loc[df15["long_name"].isin(list(df18_top["long_name"]))]
