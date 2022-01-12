import pandas as pd
import plotly.express as px
import csv
from csv import reader
import seaborn as sns
import matplotlib.pyplot as plt
FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project_Final/Modified/players_21_22.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality_name','potential','goalkeeping_reflexes'], index_col=[0])
print("*************************** Duplicates ******************************")
duplicates = FifaAll_Players_DF[FifaAll_Players_DF.duplicated()]
print(duplicates)

duplicateRowsDF = FifaAll_Players_DF[FifaAll_Players_DF.duplicated(['short_name'])]
print("Duplicate Rows based on the short name column are:", duplicateRowsDF, sep='\n')


duplicateRows_name_age_DF = FifaAll_Players_DF[FifaAll_Players_DF.duplicated(['short_name','age','height_cm'])]
print("Duplicate Rows based on the short name, age and height columns are:", duplicateRows_name_age_DF, sep='\n')

Duplicates_DF = duplicateRows_name_age_DF.groupby('short_name')['wage_eur'].agg(['mean', 'count'])
Duplicates_DF = duplicateRows_name_age_DF.sort_values(by = 'short_name', ascending = True)

fig = px.bar(Duplicates_DF[0:10], x= Duplicates_DF.index[0:10], y='short_name') # will show up to 10 seasons
fig.update_layout(title_text='Duplicate players based on short name, age and height')
fig.update_xaxes(title_text="<b> Season </b>")
fig.show()

FifaAll_Players_Drop_DF = FifaAll_Players_DF.drop(['goalkeeping_reflexes'], axis = 1)
print("*************************** Before dropping Goalkeeping column ****************************")
print(FifaAll_Players_DF.columns)
print("*************************** After dropping Goalkeeping column ****************************")
print(FifaAll_Players_Drop_DF.columns)

print("************************ Deleting rows based on certain columns *********************")
print("************************ Before delete *********************")
FifaAll_Players_DF= pd.read_csv("/users/brian/documents/FIFA_Project_Final/Modified/players_21_22.csv")
print(FifaAll_Players_DF.shape)

Fifa_Del_Test_DF = FifaAll_Players_DF.drop_duplicates(
    subset=['short_name','age','height_cm'],
    keep='last').reset_index(drop=True)

print("************************ After delete *********************")
# print latest dataframe
print(Fifa_Del_Test_DF.shape)

print("************************ After delete - End *********************")
print("************************ Duplicate Players - Begin *********************")
Found_Duplicates_DF = FifaAll_Players_DF[(FifaAll_Players_DF.short_name == 'R. Funes Mori')
                                 |(FifaAll_Players_DF.short_name == 'Mateus')]
print(Found_Duplicates_DF[['sofifa_id','short_name','age','nationality_name','dob','long_name']])

print("************************ Duplicate Players - End *********************")

print("************************ Slice - Begin *********************")
filename = "/Users/brian/Documents/FIFA_Project_Final/Modified/players_21_22.csv"

with open(filename, 'r') as data:
    for line in csv.reader(data):
        print(line[0:3])
print("************************ Slice - End *********************")
print("************************ Slice Dataframe - Begin *********************")
Slice_DF = duplicateRows_name_age_DF[2:4]# Only wanted these records from
print(Slice_DF)
print("************************ Slice Dataframe - End *********************")