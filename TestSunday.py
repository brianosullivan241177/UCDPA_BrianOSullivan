import pandas as pd
Fifa_Top_250_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv",
                   usecols=['short_name', 'height_cm', 'overall', 'club_name','potential','age','work_rate','Season','value_eur',
                            'preferred_foot','team_position','skill_ball_control','skill_dribbling','mentality_composure','wage_eur'],
                      index_col="short_name",nrows=1)
print(Fifa_Top_250_DF)