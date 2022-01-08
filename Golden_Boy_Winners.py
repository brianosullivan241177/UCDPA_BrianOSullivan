import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/AllPlayers_1.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential'], index_col=[0])
print(FifaAll_Players_DF.head()) #top records
print(FifaAll_Players_DF.dtypes) #dataframe data tyoes


text = open("/users/brian/documents/FIFA_Project/Modified/Allplayers.csv", "r")
text = ''.join([i for i in text]) \
    .replace("Renato Sanches", "Renato Sanches GB2016").replace("M. Balotelli","M. Balotelli GB2010")
x = open("/users/brian/documents/FIFA_Project/Modified/AllPlayers_1.csv","w")
x.writelines(text)
x.close()

Golden_Boy_Winners_DF = FifaAll_Players_DF[(FifaAll_Players_DF.short_name == 'M. Balotelli GB2010')
                                |(FifaAll_Players_DF.short_name == 'M. Götze')
                                |(FifaAll_Players_DF.short_name == 'Isco')
                                |(FifaAll_Players_DF.short_name == 'P. Pogba')
                                |(FifaAll_Players_DF.short_name == 'R. Sterling')
|(FifaAll_Players_DF.short_name == 'A. Martial')
|(FifaAll_Players_DF.short_name == 'Renato Sanches GB2016')
|(FifaAll_Players_DF.short_name == 'Kylian Mbappé')
|(FifaAll_Players_DF.short_name == 'M. de Ligt')
|(FifaAll_Players_DF.short_name == 'João Félix')
|(FifaAll_Players_DF.short_name == 'E. Haaland')
]
print(Golden_Boy_Winners_DF)

plot_order = Golden_Boy_Winners_DF.groupby('Season')['short_name'].sum().sort_values(ascending=False).index.values
plot_order2 = Golden_Boy_Winners_DF.sort_values(by=['Season'], inplace=True)
#sns.catplot(data=Golden_Boy_Winners_DF, x='Season',  y='overall',hue='short_name',ci=None, legend_out=False, order=plot_order2,
 #           )
a = sns.catplot(data=Golden_Boy_Winners_DF, x='Season',
                   y='wage_eur', hue='short_name', height=6, aspect=2, order=plot_order2, kind="point")
plt.legend(title='Smoker', loc='upper left', labels=['Balotelli - Winner 2010', 'Gotze Winner 2011', '3','4'])

plt.show()

