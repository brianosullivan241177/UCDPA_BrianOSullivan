import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/FIFAAllplayers_GB.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential'], index_col=[0])
print(FifaAll_Players_DF.head()) #top records
print(FifaAll_Players_DF.columns) #dataframe data tyoes

FifaAll_Players_DF.rename(columns = {'overall':'Overall'}, inplace = True)

print(FifaAll_Players_DF.columns)