import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/Allplayers.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential'], index_col=[0])

Coleman_DF = FifaAll_Players_DF[(FifaAll_Players_DF.short_name == 'S. Coleman')
                                |(FifaAll_Players_DF.short_name == 'L. Messi')]
print(Coleman_DF)

pos = list(range(len(Coleman_DF['overall'])))
width = 0.25

fig, ax = plt.subplots(figsize=(10,5))

# Setting the y axis label
ax.set_ylabel('Score')

# Setting the chart's title
ax.set_title('Test Subject Scores')

# Setting the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Setting the labels for the x ticks
ax.set_xticklabels(Coleman_DF['Season'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos) - width, max(pos) + width * 4)
plt.ylim([0, max(Coleman_DF['overall'] + Coleman_DF['potential'] + Coleman_DF['height_cm'])])

plt.bar(pos, Coleman_DF['overall'], width, alpha=0.5, color='#EE3224')
plt.bar([p + width for p in pos], Coleman_DF['potential'], width, alpha=0.5, color='#F78F1E')
plt.bar([p + width*2 for p in pos], Coleman_DF['height_cm'], width, alpha=0.5, color='#FFC222')

# Adding the legend and showing the plot
plt.legend(['Overall', 'Potential', 'Height'], loc='upper left')
plt.grid()
plt.show()
