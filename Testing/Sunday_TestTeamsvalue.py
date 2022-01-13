import pandas as pd

FifaAll_Players_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv",
                   usecols=['short_name', 'height_cm',
                            'overall', 'potential','age','work_rate','Season','league_name','club_name','mentality_composure'
                            ,'shooting','pace','passing','dribbling','defending','physic','league_name'])



name = FifaAll_Players_DF[(FifaAll_Players_DF.short_name == 'L. Messi')]
def my_func(name):
  print(f"Hello {name}! Are you from?")
