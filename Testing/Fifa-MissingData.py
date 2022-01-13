import pandas as pd
Fifa20_21_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/players_20_21.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential','gk_positioning','player_positions'], index_col=[0])

Fifa_20_top_Attack_DF = Fifa20_21_DF[Fifa20_21_DF['player_positions'].str.contains('ST|LW|RW|LW|CF|CAM|RM|LM')==True].\
    sort_values(by="overall", ascending=False)
print(Fifa_20_top_Attack_DF.head(10))

Replaced_Fifa_20_top_Attack_DF = Fifa_20_top_Attack_DF['short_name'] = Fifa_20_top_Attack_DF['gk_positioning'].fillna(0,inplace=True)
print(Replaced_Fifa_20_top_Attack_DF)
