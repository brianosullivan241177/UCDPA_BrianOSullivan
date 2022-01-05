import pandas as pd
import plotly.express as px

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/Allplayers.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential'], index_col=[0])
print(FifaAll_Players_DF.head()) #top records
print(FifaAll_Players_DF.dtypes) #dataframe data tyoes

# Irish players in the premier league - wages
Irish_Players_PL_DF = FifaAll_Players_DF[(FifaAll_Players_DF.nationality == 'Republic of Ireland') &
                                      (FifaAll_Players_DF.league_name == 'English Premier League')]
print(Irish_Players_PL_DF)
Irish_PL_wages = Irish_Players_PL_DF.groupby('Season')['wage_eur'].agg(['mean', 'count'])
Irish_PL_wages = Irish_PL_wages.sort_values(by = 'Season', ascending = True)

fig = px.bar(Irish_PL_wages[0:10], x= Irish_PL_wages.index[0:10], y='mean') # will show up to 10 seasons
fig.update_layout(title_text='Mean wages - Irish Players in the Premier League')
fig.update_xaxes(title_text="<b> Season </b>")
fig.show()

# Irish players outside the premier league - wages
Irish_Players_Excl_PL_DF = FifaAll_Players_DF[(FifaAll_Players_DF.nationality == 'Republic of Ireland') &
                                      (FifaAll_Players_DF.league_name != 'English Premier League')]
print(Irish_Players_Excl_PL_DF)
Irish_Excl_PL_wages = Irish_Players_Excl_PL_DF.groupby('Season')['wage_eur'].agg(['mean', 'count'])
Irish_Excl_PL_wages = Irish_Excl_PL_wages.sort_values(by = 'Season', ascending = True)

fig1 = px.bar(Irish_Excl_PL_wages[0:10], x= Irish_Excl_PL_wages.index[0:10], y='mean') # will show up to 10 seasons
fig1.update_layout(title_text='Mean wages - Irish Players outside the Premier League')
fig1.update_xaxes(title_text="<b> Season </b>")
fig1.show()
