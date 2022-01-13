import numpy as np
import pandas as pd

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/Allplayers.csv',


players = players.sort_values('overall_rating', ascending=False)
best_players = players[['player_api_id','player_name']].head(20)
ids = tuple(best_players.player_api_id.unique())

query = '''SELECT player_api_id, date_stat, overall_rating, potential
           FROM Player_Stats WHERE player_api_id in %s''' % (ids,)

evolution = pd.read_sql(query, conn)
evolution = pd.merge(evolution, best_players)
evolution['year'] = evolution.date_stat.str[:4].apply(int)
evolution = evolution.groupby(['year','player_api_id','player_name']).overall_rating.mean()
evolution = evolution.reset_index()

evolution.head()
