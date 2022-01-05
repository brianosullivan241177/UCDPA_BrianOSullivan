import pandas as pd
import plotly.express as px
import numpy as np

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/players_14_15_1.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential','gk_positioning','player_positions'], index_col=[0])
print(FifaAll_Players_DF.head(10)) #top records
print(FifaAll_Players_DF.dtypes) #dataframe data tyoes

print("************************* Top Midfielders ****************************")
Top_Midfielders_DF = FifaAll_Players_DF[((FifaAll_Players_DF.player_positions == 'LW')
                                               | (FifaAll_Players_DF.player_positions == 'RM')
                                               | (FifaAll_Players_DF.player_positions == 'LW, ST')
                                               | (FifaAll_Players_DF.player_positions == 'RW')
                                         & (FifaAll_Players_DF.overall >= 94))]
print(Top_Midfielders_DF)
print("************************* Sorted Midfielders ****************************")
sorted_Top_Midfielders_DF = Top_Midfielders_DF.sort_values(by='overall', ascending=False)
print(sorted_Top_Midfielders_DF)


print("*************************** Attackers ******************************")
Fifa_20_top_Attack_DF = FifaAll_Players_DF[FifaAll_Players_DF['player_positions'].str.contains('ST|LW|RW|LW|CF|CAM|RM|LM')==True].\
    sort_values(by="overall", ascending=False)
print(Fifa_20_top_Attack_DF.head(10))

#Replacing missing values
print("*************************** Replace missing values ******************************")

Replaced_Fifa_20_top_Attack_DF = FifaAll_Players_DF['short_name'] = FifaAll_Players_DF['gk_positioning'].fillna(0,inplace=True)
print(Replaced_Fifa_20_top_Attack_DF)

print("*************************** Duplicates ******************************")
Fifa_Duplcates = FifaAll_Players_DF.duplicated(subset=None, keep='first')
print(Fifa_Duplcates)


print("*************************** Find duplicates *********************")
duplicate = FifaAll_Players_DF[FifaAll_Players_DF.duplicated()]

print("Duplicate Rows :")

# Print the resultant Dataframe
print(duplicate)
print("************************** Players after filling in gk_positioning ******************************")
print(FifaAll_Players_DF.head(10))