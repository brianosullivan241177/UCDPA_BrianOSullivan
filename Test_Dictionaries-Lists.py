import csv
import numpy as np
import pandas as pd
print("*********************************** List [] - Begin ****************************************")
filename = "/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv"

with open(filename, 'r') as data:
    for line_list in csv.reader(data):
        print(line_list)
print("*********************************** List [] - End ****************************************")

print("*********************************** Dictionary {}- Begin ****************************************")

filename_dict = "/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv"
with open(filename_dict, 'r') as data:
    for line_dict in csv.DictReader(data):
        print(line_dict)
print("*********************************** Dictionary {} - End ****************************************")

print("*********************************** List - certain fields ****************************************")
print(line_list[0:5])
print(len(line_list))
print("*********************************** List - certain fields - End ****************************************")

print("*************** Testing ***************")

def all_values(dict_obj):
    ''' This function generates all values of
        a nested dictionary.
    '''
    # Iterate over all values of the dictionary
    for key , value in line_dict.items():
        # If value is of dictionary type then yield all values
        # in that nested dictionary
        if isinstance(value, dict):
            for v in all_values(value):
                yield v
        else:
            yield value
# Iterate over all values of a nested dictionary
# and print them one by one.
for value in all_values('player_url'):
    print(value)

data = list(line_dict.items())
an_array = np.array(data)
print(an_array)

dictValues = list (line_dict.values())
print(dictValues)