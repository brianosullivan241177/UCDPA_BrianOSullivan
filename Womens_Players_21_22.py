import pandas as pd

import matplotlib.pyplot as plt

Fifa_Top_250_W_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project_Final/Modified/female_players_21_22.csv",
                   usecols=['short_name', 'height_cm', 'overall','league_name', 'club_name','potential','age','work_rate','Season','value_eur',
                            'preferred_foot','club_position','skill_ball_control','player_positions','goalkeeping_reflexes','goalkeeping_speed','skill_dribbling','mentality_composure','wage_eur'],
                      index_col="short_name",nrows=250)

print("***************** Merging Data Frames - Begin ************************")
fifa_20_potential = Fifa_Top_250_W_DF[(Fifa_Top_250_W_DF.age.astype(int)>=18) & (Fifa_Top_250_W_DF.age.astype(int)<=40)].groupby(['age'])['potential'].mean()
fifa_20_overall = Fifa_Top_250_W_DF[(Fifa_Top_250_W_DF.age.astype(int)>=18) & (Fifa_Top_250_W_DF.age.astype(int)<=40)].groupby(['age'])['overall'].mean()
fifa_20_summary = pd.concat([fifa_20_potential, fifa_20_overall], axis=1)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(fifa_20_summary)
plt.legend(['Avg. Potential', 'Avg. Overall'], loc='upper right')
ax.set_xlabel("Age")
ax.set_ylabel("Avg. Potential Rating - Avg. Overall Rating in % ")
ax.set_title("Player avg. Potential rating v avg. Overall rating by age for the top 250 players")
plt.show()