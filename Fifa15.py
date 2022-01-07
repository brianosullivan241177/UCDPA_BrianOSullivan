import os, glob
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from csv import writer
from csv import reader

def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)

header_of_new_col = 'Season'
default_text = '2014-2015'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project/players_15.csv', '/Users/brian/Documents/FIFA_Project/players_14_15.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2015-2016'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project/players_16.csv', '/Users/brian/Documents/FIFA_Project/players_15_16.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2016-2017'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project/players_17.csv', '/Users/brian/Documents/FIFA_Project/players_16_17.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2017-2018'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project/players_18.csv', '/Users/brian/Documents/FIFA_Project/players_17_18.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2018-2019'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project/players_19.csv', '/Users/brian/Documents/FIFA_Project/players_18_19.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2019-2020'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project/players_20.csv', '/Users/brian/Documents/FIFA_Project/players_19_20.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2020-2021'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project/players_21.csv', '/Users/brian/Documents/FIFA_Project/players_20_21.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))


Fifa15_DF = pd.read_csv('/Users/brian/Documents/FIFA_Project/players_15.csv',
                           usecols=['league_name','short_name','club_name','wage_eur','league_name','preferred_foot', 'overall','age','work_rate','nationality'], index_col=[1])
print(Fifa15_DF.head()) #top records
print(Fifa15_DF.dtypes) #dataframe data tyoes




English_PL_Relegated_20142015_DF = Fifa15_DF[(Fifa15_DF.league_name == 'English Premier League') & ((Fifa15_DF.club_name == 'Hull City')
                                                                                           | (Fifa15_DF.club_name == 'Burnley')
                                                                                           | (Fifa15_DF.club_name == 'Queens Park Rangers'))] #Premier League players
print(English_PL_Relegated_20142015_DF) #Premier League relegated players - top records


print("********************** 2014 - 2015 Escaped Relegation - Start **********************")
English_PL_Escaped_Relegation_20142015_DF=Fifa15_DF[(Fifa15_DF.league_name == 'English Premier League') & ((Fifa15_DF.club_name == 'Newcastle United')
                                                                                                  | (Fifa15_DF.club_name == 'Sunderland')
                                                                                                  | (Fifa15_DF.club_name == 'Aston Villa'))] #Premier League players
print(English_PL_Escaped_Relegation_20142015_DF) #Premier League escaped relegatio players - top records
print("********************** 2014 - 2015 Escaped Relegation - End **********************")

Feet_Type = English_PL_Relegated_20142015_DF.preferred_foot.value_counts()
print(Feet_Type)

def as_thousands(value):
    return value / 10_000
English_PL_Escaped_Relegation_20142015_DF[['wage_eur','club_name']].groupby('club_name') \
                                            .sum() \
                                            .sort_values('wage_eur', ascending=False) \
                                            .head(10) \
                                            .apply(as_thousands) \
                                            .plot(kind='barh', figsize=(11,6))

plt.xlabel("")
plt.ylabel('Salary')
plt.title('Weekly Salary in Thousands - Escaped Relegation');
plt.show()


English_PL_Relegated_20142015_DF[['wage_eur','club_name']].groupby('club_name') \
                                            .sum() \
                                            .sort_values('wage_eur', ascending=False) \
                                            .head(10) \
                                            .apply(as_thousands) \
                                            .plot(kind='barh', figsize=(11,6))

plt.xlabel("")
plt.ylabel('Salary')
plt.title('Weekly Salary in Thousands - Relegated');
plt.show()

Combined_DF = [English_PL_Relegated_20142015_DF, English_PL_Escaped_Relegation_20142015_DF]
print (Combined_DF)


Combined_DF[['wage_eur','club_name']].groupby('club_name') \
                                            .sum() \
                                            .sort_values('wage_eur', ascending=False) \
                                            .head(10) \
                                            .apply(as_thousands) \
                                            .plot(kind='barh', figsize=(11,6))

plt.xlabel("")
plt.ylabel('Salary')
plt.title('allteams');
plt.show()
