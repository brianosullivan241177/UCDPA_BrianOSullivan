import pandas as pd

Fifa_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv",
                   usecols=['short_name', 'height_cm', 'overall', 'potential','age','work_rate','Season','league_name','club_name'],nrows=10)

for index, row in Fifa_DF.iterrows():
    print(row)

row = next(Fifa_DF.iterrows())[1]

for index, row in Fifa_DF.head(n=2).iterrows():
     print(index, row)


     # iterate over rows with iterrows()
     for index, row in Fifa_DF.head().iterrows():
         # access data using column names
         print(index, row['short_name'], row['overall'], row['age'])


Fifa_All_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv",
                   usecols=['short_name', 'height_cm', 'overall', 'potential','age','work_rate','Season','league_name','club_name'])

Coleman_DF = Fifa_All_DF[(Fifa_All_DF.short_name == 'S. Coleman')]
print(Coleman_DF)
Coleman_Sort_DF = Coleman_DF.sort_values(by=['Season', 'potential'], inplace=True, ascending=False)
for index, row in Coleman_DF.iterrows():
    print(index, ': ', row['short_name'], 'had the potential of',row['potential'],'in season',row['Season'] )

