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
    .replace("Renato Sanches", "GB Winner 2016 Renato Sanches").replace("M. Balotelli","GB Winner 2010 M. Balotelli").\
    replace("M. Götze", "GB Winner 2011 M. Götze").replace("Isco", "GB Winner 2012 Isco").\
    replace("P. Pogba", "GB Winner 2013 P. Pogba").replace("R. Sterling", "GB Winner 2014 R. Sterling").\
    replace("A. Martial", "GB Winner 2015 A. Martial").replace("M. de Ligt", "GB Winner 2018 M. de Ligt").\
    replace("João Félix", "GB Winner 2019 João Félix").replace("E. Haaland", "GB Winner 2020 E. Haaland".\
replace("K. Mbappe Lottin", "GB Winner 2017 K. Mbappé")
)

x = open("/users/brian/documents/FIFA_Project/Modified/AllPlayers_2.csv","w")
x.writelines(text)
x.close()

text = open("/users/brian/documents/FIFA_Project/Modified/Allplayers_2.csv", "r")
text = ''.join([i for i in text]) \
    .replace("Renato Sanches", "GB Winner 2016 Renato Sanches").replace("M. Balotelli","GB Winner 2010 M. Balotelli").\
    replace("M. Götze", "GB Winner 2011 M. Götze").replace("Isco", "GB Winner 2012 Isco").\
    replace("P. Pogba", "GB Winner 2013 P. Pogba").replace("R. Sterling", "GB Winner 2014 R. Sterling").\
    replace("A. Martial", "GB Winner 2015 A. Martial").replace("M. de Ligt", "GB Winner 2018 M. de Ligt").\
    replace("João Félix", "GB Winner 2019 João Félix").replace("E. Haaland", "GB Winner 2020 E. Haaland".\
replace("K. Mbappé", "GB Winner 2017 K. Mbappé")
)

x = open("/users/brian/documents/FIFA_Project/Modified/AllPlayers_3.csv","w")
x.writelines(text)
x.close()

Golden_Boy_Winners_DF = FifaAll_Players_DF[
    (FifaAll_Players_DF.short_name == 'GB Winner 2010 M. Balotelli')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2011 M. Götze')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2012 Isco')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2013 P. Pogba')
    |(FifaAll_Players_DF.short_name == 'GB Winner 2014 R. Sterling')
#    |(FifaAll_Players_DF.short_name == 'GB Winner 2015 A. Martial')
#    |(FifaAll_Players_DF.short_name == 'GB Winner 2016 Renato Sanches')
#    |(FifaAll_Players_DF.short_name == 'GB Winner 2017 K. Mbappé')
#    |(FifaAll_Players_DF.short_name == 'GB Winner 2018 M. de Ligt')
#    |(FifaAll_Players_DF.short_name == 'GB Winner 2019 João Félix"')
#    |(FifaAll_Players_DF.short_name == 'GB Winner 2020 E. Haaland')
]
print(Golden_Boy_Winners_DF)

plot_order = Golden_Boy_Winners_DF.groupby('Season')['short_name'].sum().sort_values(ascending=False).index.values
plot_order2 = Golden_Boy_Winners_DF.sort_values(by=['Season'], inplace=True)
#sns.catplot(data=Golden_Boy_Winners_DF, x='Season',  y='overall',hue='short_name',ci=None, legend_out=False, order=plot_order2,
 #           )
a = sns.catplot(data=Golden_Boy_Winners_DF, x='Season',
                   y='overall', hue='short_name', height=6, aspect=2, order=plot_order2, kind="point")


a = sns.catplot(data=Golden_Boy_Winners_DF, x='Season',
                   y='wage_eur', hue='short_name', height=6, aspect=2, order=plot_order2, kind="point")
plt.show()

