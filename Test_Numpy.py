import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Fifa_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv",
                   usecols=['short_name', 'height_cm', 'overall','mentality_composure','age'],nrows=10)

print("***************** Numpy   ******************")
import numpy as np
import csv
with open("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv", 'r') as f:
    allplayers = list(csv.reader(f, delimiter=";"))
print("***************** Numpy array Top 5 - Begin ******************")
allplayers1 = np.array(allplayers[0:6])
print(allplayers1)
print("***************** Numpy array Top 5 - End ********************")
print("***************** Third player in list - Begin  ******************")
third_player = allplayers1[3,:]
print(third_player)
print("***************** Third player in list - End *********************")
print("************* list datatypes")


#print(allplayers1.dtype)

print("********************** - New way *************************")
arrays2021 = [np.array(map(int, line.split())) for line in open('/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv')]
#print(arrays2021)

arrays2020 = [np.array(map(int, line.split())) for line in open('/Users/brian/Documents/FIFA_Project/Modified/players_19_20.csv')]
#print(arrays2020)

#from numpy import genfromtxt
#my_data = genfromtxt("/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv", delimiter=',',usecols=np.arange(0,187))

print("********************** - Type of arrays *************************")
print(type(arrays2021)) #list
print(type(arrays2020)) #list

print("********************** - Combined - Begin ************************")

fifa_20_21 = pd.read_csv('/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv',usecols =['short_name','overall','potential','club_name','gk_positioning'])
fifa_20_21['Season'] = 2021
fifa_19_20 = pd.read_csv('/Users/brian/Documents/FIFA_Project/Modified/players_19_20.csv',usecols= ['short_name','overall','potential','club_name','gk_positioning'])
fifa_19_20['Season'] = 2020
print("********************** fifa_19_20 shape  ************************")
print(fifa_19_20.shape)
print("********************** fifa_20_21 shape  ************************")
print(fifa_20_21.shape)
fifas_merged = pd.concat([fifa_20_21,fifa_19_20],ignore_index=True)
fifas_merged['Lastname'] = fifas_merged['short_name'].str.split(' ').str[-1]
fifas_merged = fifas_merged.drop(columns = ['gk_positioning'])
print("********************** Merged shape  ************************")
print(fifas_merged.shape)
print("********************** Duplicates in merged file  ************************")
Duplicates_DF = fifas_merged.sort_values(by = 'short_name', ascending = True)
print(Duplicates_DF)
print("********************** Duplicates in merged file  ************************")