import pandas as pd

Fifa_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv",
                   usecols=['short_name', 'height_cm', 'overall', 'potential','age','work_rate','Season'], index_col="short_name")

print("************************* Top 20 players ****************************")
print(Fifa_DF.head(20))

print("************************* Salah and Messi using loc ****************************")
rows= Fifa_DF.loc[["L. Messi", "M. Salah"]]
print(type(rows))
print(rows.head(17))

print("************************* List Index ****************************")
print(list(rows.index))
print("************************* First 500 records iloc ****************************")

Fifa_Col_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv",
                   usecols=['sofifa_id', 'short_name', 'height_cm', 'overall', 'potential','age','Season','dob'], index_col=[0],nrows=500)

print(Fifa_Col_DF)
print("************************** ")
print(list(Fifa_Col_DF.index))
print("************************* iloc example ********************************")
iloc_test = Fifa_Col_DF.iloc[0:5]
print(iloc_test)

print("******************************** Slicing *********************************")

Messi_Slicing_DF = Fifa_Col_DF.loc[(Fifa_Col_DF["short_name"] == "L. Messi"),

               ["short_name", "overall","potential","age","Season"]]

print(Messi_Slicing_DF)

import pandas as pd


Sort_DF = pd.DataFrame(Fifa_Col_DF, columns=['short_name','overall', 'potential', 'Season'])

# sort by multiple columns: Year and Brand
Sort_DF.sort_values(by=['overall', 'potential'], inplace=True, ascending=False)

print(Sort_DF)

#Sort_DF.loc[0, ['short_name', 'overall', 'Season']]