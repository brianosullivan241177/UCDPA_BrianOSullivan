import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/Players_14_15.csv',
    usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential'], index_col=[0])

print(FifaAll_Players_DF)
print(FifaAll_Players_DF.dtypes)

Top_Scorers_14_15_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/Top_Scorers_14_15.csv',index_col=[0])
print(Top_Scorers_14_15_DF)
print(Top_Scorers_14_15_DF.dtypes)


merged_inner = pd.merge(left=Top_Scorers_14_15_DF, right=FifaAll_Players_DF, left_on='short_name', right_on='short_name')
print(merged_inner)

#Irish_PL_wages = merged_inner.groupby('Season')['wage_eur'].agg(['mean', 'count'])
#Irish_PL_wages = merged_inner.sort_values(by = 'Season', ascending = True)


#fig = px.bar(Irish_PL_wages[0:10], x= Irish_PL_wages.index[0:10], y='short_name') # will show up to 10 seasons
#fig.update_layout(title_text='Mean wages - Irish Players in the Premier League')
#fig.update_xaxes(title_text="<b> Season </b>")
#plt.show()

plot_order = merged_inner.sort_values(by=['Season'], inplace=True)
# Graph to show overall ratings by Golden Boy winner - R. Sterling continuing to improve
a = sns.catplot(data=merged_inner, x='Season',
                   y='overall', hue='short_name', height=6, aspect=2, order=plot_order, kind="point")
plt.show()

plt.figure(figsize=(12,10))
sns.histplot(x="short_name",
             data=merged_inner,
             hue="Goals Scored",
             multiple="dodge",
             palette="plasma"
            )
plt.show()
