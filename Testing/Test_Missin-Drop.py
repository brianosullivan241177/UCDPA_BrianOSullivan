import pandas as pd

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/players_19_20.csv',
                           usecols=['sofifa_id','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential','gk_positioning','player_positions'], index_col=[0])
print(FifaAll_Players_DF.head(10)) #top records
print(FifaAll_Players_DF.dtypes) #dataframe data types

print("*************************** Attackers ******************************")
Fifa_20_top_Attack_DF = FifaAll_Players_DF[FifaAll_Players_DF['player_positions'].str.contains('ST|LW|RW|LW|CF|CAM|RM|LM')==True].\
    sort_values(by="overall", ascending=False)
print(Fifa_20_top_Attack_DF.head(10))

#Replacing missing values
print("*************************** Replace missing values - Begin ******************************")
Replaced_Fifa_20_top_Attack_DF =  Fifa_20_top_Attack_DF['gk_positioning'].fillna(0,inplace=True)
print("*************************** Replace missing values - End ********************************")

print("************************** Players after filling in gk_positioning ******************************")
print(Fifa_20_top_Attack_DF.head(10))
