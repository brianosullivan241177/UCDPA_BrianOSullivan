import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/players_20_21.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential','goalkeeping_reflexes'], index_col=[0])
print("*************************** Duplicates ******************************")
duplicates = FifaAll_Players_DF[FifaAll_Players_DF.duplicated()]

print(duplicates)

duplicateRowsDF = FifaAll_Players_DF[FifaAll_Players_DF.duplicated(['short_name'])]
print("Duplicate Rows based on the short name column are:", duplicateRowsDF, sep='\n')


duplicateRows_name_age_DF = FifaAll_Players_DF[FifaAll_Players_DF.duplicated(['short_name','age','height_cm'])]
print("Duplicate Rows based on the short name, age and height columns are:", duplicateRows_name_age_DF, sep='\n')

Irish_PL_wages = duplicateRows_name_age_DF.groupby('short_name')['wage_eur'].agg(['mean', 'count'])
Irish_PL_wages = duplicateRows_name_age_DF.sort_values(by = 'short_name', ascending = True)

fig = px.bar(Irish_PL_wages[0:10], x= Irish_PL_wages.index[0:10], y='short_name') # will show up to 10 seasons
fig.update_layout(title_text='Duplicate players based on short name, age and height')
fig.update_xaxes(title_text="<b> Season </b>")
fig.show()


FifaAll_Players_Drop_DF = FifaAll_Players_DF.drop(['goalkeeping_reflexes'], axis = 1)
print("*************************** Before dropping Goalkeeping column ****************************")
print(FifaAll_Players_DF.columns)
print("*************************** After dropping Goalkeeping column ****************************")
print(FifaAll_Players_Drop_DF.columns)

