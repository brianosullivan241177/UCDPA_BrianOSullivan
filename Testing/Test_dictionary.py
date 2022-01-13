import pandas as pd
brics = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv",index_col=0)
print(brics)

brics.index=[sofifa_id]
