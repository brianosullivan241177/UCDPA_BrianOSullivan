import csv

filename_dict = "/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv"
with open(filename_dict, 'r') as data:
    for line_dict in csv.DictReader(data):
        print(line_dict)

first_value = list(line_dict.values())[0]
print('First Value: ', first_value)

n = 3
# Get first 3 values of a record in a dictionary
first_n_values = list(line_dict.values())[:3]
print('First 3 Values:')
print(first_n_values)

Nrow = 3
# Get first row of values in a dictionary
first_n_values = list(line_dict.values())[0:]
print('First 3 Values:')
print(first_n_values)

keys = ['short_name', 'age']
for key in keys:
    line_dict.get(key)
    print(key)
