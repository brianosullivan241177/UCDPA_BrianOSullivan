import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

Fifa_Top_250_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/AllPlayers_1.csv",
                   usecols=['short_name', 'sofifa_id','height_cm', 'overall', 'club_name','potential','age','work_rate','Season','value_eur',
                            'preferred_foot','team_position','skill_ball_control','skill_dribbling','mentality_composure'],
                      index_col="short_name")
print(Fifa_Top_250_DF.head(50))

Coleman_DF = Fifa_Top_250_DF[(Fifa_Top_250_DF.short_name == "H. Kane")]

#print(Coleman_DF)
