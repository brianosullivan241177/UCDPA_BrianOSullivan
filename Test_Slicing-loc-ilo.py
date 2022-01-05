import pandas as pd

Fifa15 = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv",
                   usecols=['short_name', 'height_cm', 'overall', 'potential','age','work_rate','Season'], index_col="short_name")

print("************************* Top 20 players ****************************")
print(Fifa15.head(200))

print("************************* Salah and Messi ****************************")
rows= Fifa15.loc[["L. Messi"]]
print(type(rows))
print(rows.head(10))