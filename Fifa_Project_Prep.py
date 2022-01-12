# *********************** Brian O'Sullivan ***********************
# ********************** Fifa Project - Prep *********************
# ***** Add a column to each yearly csv file and then combine ****
# * https://github.com/brianosullivan241177/UCDPA_BrianOSullivan *


import os, glob
from csv import writer
from csv import reader
import pandas as pd

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
add_column_in_csv('/Users/brian/Documents/FIFA_Project_Final/players_15.csv', '/Users/brian/Documents/FIFA_Project_Final/Modified/players_14_15.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2015-2016'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project_Final/players_16.csv', '/Users/brian/Documents/FIFA_Project_Final/Modified/players_15_16.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2016-2017'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project_Final/players_17.csv', '/Users/brian/Documents/FIFA_Project_Final/Modified/players_16_17.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2017-2018'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project_Final/players_18.csv', '/Users/brian/Documents/FIFA_Project_Final/Modified/players_17_18.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2018-2019'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project_Final/players_19.csv', '/Users/brian/Documents/FIFA_Project_Final/Modified/players_18_19.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2019-2020'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project_Final/players_20.csv', '/Users/brian/Documents/FIFA_Project_Final/Modified/players_19_20.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2020-2021'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project_Final/players_21.csv', '/Users/brian/Documents/FIFA_Project_Final/Modified/players_20_21.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))

header_of_new_col = 'Season'
default_text = '2021-2022'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project_Final/players_22.csv', '/Users/brian/Documents/FIFA_Project_Final/Modified/players_21_22.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))
#merge all the files that you are going to work on
path = "/users/brian/documents/FIFA_Project_Final/Modified/"
all_files = glob.glob(os.path.join(path, "p*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True, sort=False)
df_merged.to_csv("/users/brian/documents/FIFA_Project_Final/Modified/FIFAAllplayersM.csv") #This part to create file you will use for majority of the project