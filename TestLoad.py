import os, glob
import pandas as pd

path = "/users/brian/documents/fifatest1/"
all_files = glob.glob(os.path.join(path, "p*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True, sort=False)
df_merged.to_csv("/users/brian/documents/fifatest1/allplayers.csv")
AllPlayersDF = pd.read_csv('/Users/brian/Documents/fifatest1/allplayers.csv',
                           usecols=['short_name', 'height_cm', 'overall', 'potential','age','work_rate','attacking_finishing',
                                    'movement_agility','mentality_composure'], index_col="short_name")
print(AllPlayersDF.head())

GoldenBoy2014= AllPlayersDF.loc[["A. Martial"]]
print(GoldenBoy2014)