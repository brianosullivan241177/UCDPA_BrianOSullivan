import os, glob
import pandas as pd
import numpy as np
import seaborn as sns
#path = "/users/brian/documents/fifatest1/"
#all_files = glob.glob(os.path.join(path, "p*.csv"))
#df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
#df_merged = pd.concat(df_from_each_file, ignore_index=True, sort=False)
#df_merged.to_csv("/users/brian/documents/fifatest1/allplayers.csv")
AllPlayersDF = pd.read_csv('/Users/brian/Documents/fifatest1/allplayers.csv',
                           usecols=['short_name', 'potential', 'overall','age','work_rate','attacking_finishing',
                                    'movement_agility','mentality_composure','club'], index_col="short_name")
print(AllPlayersDF.head())

GoldenBoy2015= AllPlayersDF.loc[["A. Martial"]]
print(GoldenBoy2015)
GoldenBoy2016= AllPlayersDF.loc[["Renato Sanches"]]
print(GoldenBoy2016)


import matplotlib.pyplot as plt
medals = pd.read_csv("/Users/brian/Documents/fifatest1/allplayers.csv",
                   usecols=['short_name', 'potential', 'overall','age','work_rate','attacking_finishing',
                                    'movement_agility','mentality_composure'], index_col="short_name")
fig, ax = plt.subplots()
x = np.arange(5)
GoldenBoy2015.plot.bar(x="age", rot=70, title="Golden Boy 2015")
plt.xticks(x, ['18', '19', '20', '21', '22'])
plt.show(block=True)

# Create a sample dataframe with an text index
#plotdata = GoldenBoy2015.DataFrame("overall","age")
# Plot a bar chart
#plotdata.plot(kind="bar")
#print("************ GoldenBoy 2015 ************")
#print(GoldenBoy2015)
#print(type(GoldenBoy2015))
#X = list(GoldenBoy2015.loc[:, ['age']]) #Age
#Y = list(GoldenBoy2015.loc[:, ['overall']]) #Overall
#plt.bar(X, Y, color='r')
#plt.title("2015 Golden Boy")
#plt.xlabel("Ages")
#plt.ylabel("Overall")
#plt.show()
print("************ GoldenBoy 2015 ************")
