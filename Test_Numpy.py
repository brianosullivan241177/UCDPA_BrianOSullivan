import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from math import pi #Used in Radar Plots
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
import warnings
Fifa_DF = pd.read_csv("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv",
                   usecols=['short_name', 'height_cm', 'overall','mentality_composure','age'],nrows=1)
print(Fifa_DF.dtypes)

import csv
with open("/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv", 'r') as f:
    allplayers = list(csv.reader(f, delimiter=";"))
import numpy as np
allplayers1 = np.array(allplayers[0:5])
print(allplayers1)
print("***************** Third player in list   ******************")
third_player = allplayers1[3,:]
print(third_player)
print("************* list datatypes")


print(allplayers1.dtype)

print("********************** - New way *************************")
arrays2021 = [np.array(map(int, line.split())) for line in open('/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv')]
print(arrays2021)

arrays2020 = [np.array(map(int, line.split())) for line in open('/Users/brian/Documents/FIFA_Project/Modified/players_19_20.csv')]
print(arrays2020)

#from numpy import genfromtxt
#my_data = genfromtxt("/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv", delimiter=',',usecols=np.arange(0,187))

print("********************** - Type of arrays *************************")
print(type(arrays2021)) #list
print(type(arrays2020)) #list

print("********************** - Combined ************************")
arr = np.concatenate((arrays2020, arrays2021), axis=0)
print(arr)

plt.figure(dpi=125)
sns.displot(a=Fifa_DF['age'],kde=False,bins=20)
plt.axvline(x=np.mean(Fifa_DF['age']),c='green',label='Mean Age of All Players')
plt.legend()
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Age')
#plt.show()

fifa_20_21 = pd.read_csv('/Users/brian/Documents/FIFA_Project/Modified/players_20_21.csv',usecols = ['short_name','overall','potential','club_name'])
fifa_20_21['Season'] = 2021
fifa_19_20 = pd.read_csv('/Users/brian/Documents/FIFA_Project/Modified/players_19_20.csv',usecols = ['short_name','overall','potential','club_name'])
fifa_19_20['Season'] = 2020


fifas_merged = pd.concat([fifa_20_21,fifa_19_20],ignore_index=True)
fifas_merged['Lastname'] = fifas_merged['short_name'].str.split(' ').str[-1]
fifas_merged = fifas_merged.drop(columns = ['short_name'])
print(fifas_merged.head(15000))
