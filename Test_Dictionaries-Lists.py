import csv
print("*********************************** List [] - Begin ****************************************")
filename = "/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv"

with open(filename, 'r') as data:
    for line in csv.reader(data):
        print(line)
print("*********************************** List [] - End ****************************************")

print("*********************************** Dictionary {}- Begin ****************************************")

#filename_dict = "/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv"


#with open(filename_dict, 'r') as data:
 #   for line in csv.DictReader(data):
  #      print(line)
print("*********************************** Dictionary {} - End ****************************************")