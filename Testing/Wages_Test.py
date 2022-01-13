import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Fifa_Top_250_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project_Final/Modified/players_21_22.csv",
                   usecols=['short_name', 'height_cm', 'overall','league_name', 'club_name','potential','age','work_rate','Season','value_eur',
                            'preferred_foot','club_position','skill_ball_control','player_positions','goalkeeping_reflexes','goalkeeping_speed','skill_dribbling','mentality_composure','wage_eur'],
                      index_col="short_name",nrows=250)

fifa_20_potential = Fifa_Top_250_DF[(Fifa_Top_250_DF.age.astype(int)>=18) & (Fifa_Top_250_DF.age.astype(int)<=40)].groupby(['preferred_foot'])['potential'].mean()
fifa_20_overall = Fifa_Top_250_DF[(Fifa_Top_250_DF.age.astype(int)>=18) & (Fifa_Top_250_DF.age.astype(int)<=40)].groupby(['league_name'])['overall'].mean()
fifa_20_summary = pd.concat([fifa_20_potential, fifa_20_overall], axis=1)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(fifa_20_summary)
plt.legend(['Avg. Potential', 'Avg. Overall'], loc='upper right')
ax.set_xlabel("Age")
ax.set_ylabel("Avg. Potential Rating - Avg. Overall Rating in % ")
ax.set_title("Player avg. Potential rating v avg. Overall rating by age for the top 250 players")
plt.show()
