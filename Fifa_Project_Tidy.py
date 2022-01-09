import pandas as pd
import plotly.express as px
FifaAll_Players_DF = pd.read_csv('/users/brian/documents/FIFA_Project/Modified/Allplayers.csv',
                           usecols=['sofifa_id','short_name','league_name','club_name','wage_eur', 'overall','age','preferred_foot',
                                    'Season', 'height_cm','nationality','potential'], index_col=[0])
print(FifaAll_Players_DF.head()) #top records
print(FifaAll_Players_DF.dtypes) #dataframe data tyoes

# Irish players in the premier league - wages
Irish_Players_PL_DF = FifaAll_Players_DF[(FifaAll_Players_DF.nationality == 'Republic of Ireland') &
                                      (FifaAll_Players_DF.league_name == 'English Premier League')]
print(Irish_Players_PL_DF)
Irish_PL_wages = Irish_Players_PL_DF.groupby('Season')['wage_eur'].agg(['mean', 'count'])
Irish_PL_wages = Irish_PL_wages.sort_values(by = 'Season', ascending = True)

fig = px.bar(Irish_PL_wages[0:20], x= Irish_PL_wages.index[0:20], y='mean')
fig.update_layout(title_text='Mean wages - Irish Players in the Premier League')
fig.update_xaxes(title_text="<b> Season </b>")
fig.show()

# Irish players outside the premier league - wages
Irish_Players_Excl_PL_DF = FifaAll_Players_DF[(FifaAll_Players_DF.nationality == 'Republic of Ireland') &
                                      (FifaAll_Players_DF.league_name != 'English Premier League')]
print(Irish_Players_Excl_PL_DF)
Irish_Excl_PL_wages = Irish_Players_Excl_PL_DF.groupby('Season')['wage_eur'].agg(['mean', 'count'])
Irish_Excl_PL_wages = Irish_Excl_PL_wages.sort_values(by = 'Season', ascending = True)

fig1 = px.bar(Irish_Excl_PL_wages[0:20], x= Irish_Excl_PL_wages.index[0:20], y='mean')
fig1.update_layout(title_text='Mean wages - Irish Players outside the Premier League')
fig1.update_xaxes(title_text="<b> Season </b>")
fig1.show()



#English_PL_Relegated_20142015_DF = FifaAll_Players_DF[(FifaAll_Players_DF.league_name == 'English Premier League') &
#                                             (FifaAll_Players_DF.Season == '2014-2015') &
 #                                            ((FifaAll_Players_DF.club_name == 'Hull City')
  #                                             | (FifaAll_Players_DF.club_name == 'Burnleys')
   #                                            | (FifaAll_Players_DF.club_name == 'Queens Park Rangerss'))] #Premier League players
#print(English_PL_Relegated_20142015_DF) #Premier League relegated players - top records

#print("********************** 2014 - 2015 Escaped Relegation - Start **********************")
#English_PL_Escaped_Relegation_20142015_DF=FifaAll_Players_DF[(FifaAll_Players_DF.league_name == 'English Premier League') &
 #                                                           (FifaAll_Players_DF.Season == '2014-2015') &
  #                                                          ((FifaAll_Players_DF.club_name == 'Newcastle United')
   #                                                         | (FifaAll_Players_DF.club_name == 'Sunderlands')
    #                                                        | (FifaAll_Players_DF.club_name == 'Aston Villas'))] #Premier League players
#print(English_PL_Escaped_Relegation_20142015_DF) #Premier League escaped relegatio players - top records
#print("********************** 2014 - 2015 Escaped Relegation - End **********************")

print("******************************* Combined - Start  ****************************************")
#Combined_DF = [English_PL_Relegated_20142015_DF, English_PL_Escaped_Relegation_20142015_DF]
#print (Combined_DF)


print("******************************* Merged ****************************************")

#plt.figure(figsize=(14,5))
#plt.title('Age Distribution FIFA 20')
#sns.distplot(a=English_PL_Relegated_20142015_DF['age'], kde=True, bins=20)
#plt.axvline(x=np.mean(English_PL_Relegated_20142015_DF['age']),c='orange',label='Mean Age of All Players')
#plt.legend()
#plt.show()
