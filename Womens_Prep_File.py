
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
default_text = '2021-2022'
# Add the column season to csv file with season information
add_column_in_csv('/Users/brian/Documents/FIFA_Project_Final/female_players_22.csv',
                  '/Users/brian/Documents/FIFA_Project_Final/Modified/female_players_21_22.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(
                      default_text))
