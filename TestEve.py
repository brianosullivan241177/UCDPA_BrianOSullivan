
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def Club(x):
    return dataset[dataset['club'] == x ][
        ['short_name','age','club',"player_positions","potential","value_eur"]].sort_values(by=['potential'],ascending=False)
def Country(x):
    return dataset[dataset['nationality'] == x ][['short_name','age','nationality',"player_positions",
                                            "potential","value_eur"]].sort_values(by=['potential'],ascending=False)

dataset=pd.read_csv('/Users/brian/Documents/FIFA_Project/Modified/Allplayers.csv')

potential_attribute = dataset.sort_values(by ='potential', ascending=False).head()
potential_attribute

skillers = dataset[(dataset["skill_moves"] == 4) | (dataset["skill_moves"] == 5)]
skiller_nations = skillers["nationality"].value_counts(normalize=True)
rest = skiller_nations[10:].sum()
skiller_nations = skiller_nations[:10]
skiller_nations["Other"] = rest
pie, ax = plt.subplots(figsize=[12,12])
labels = skiller_nations.keys()
plt.pie(x=skiller_nations, autopct="%.1f%%", labels=labels, pctdistance=0.5, explode=[0.05]*11);
plt.legend(loc="upper right")
plt.title("Skill moves and countries", fontsize=14);

def find_min_max_in(col):
    top = dataset[col].idxmax()
    top_df = pd.DataFrame(dataset.loc[0])

    bottom = dataset[col].idxmin()
    bottom_df = pd.DataFrame(dataset.loc[1])

    info_df = pd.concat([top_df, bottom_df], axis=1)
    return info_df


find_min_max_in('wage_eur')

dataset[dataset['potential'] >= 93]
def create_polarcharts(
        stats: list,
        color: str,
        img_link: str,
        name_one: str,
        name_two: str
):
    '''
    The function accepts the following arguments:

        stats - takes a list of numeric values of characteristics
        color - takes the color of the lines in the diagram
        img_link - accepts a link to an image of a football player
        name_one - takes the name of the footballer
        name_two - accepts any additional text

    '''
    # Determine the number of rows and columns
    fig = make_subplots(rows=1, cols=2,
                        # We indicate the types of graphs in each block
                        specs=[[{'type': 'xy'}, {"type": "polar"}]],
                        # Setting the width of each column
                        column_widths=[0.5, 0.5])

    # Create a Polar Chart
    fig.add_trace(go.Scatterpolar(
        # Passing numeric parameters
        r=stats,
        # Passing parameter names
        theta=['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physic', 'Pace'],
        # Setting the fill parameter
        fill='toself',
        # Specify the signature on hover
        hovertemplate='<b>%{theta}</b>' + f'<b>: ' + '%{r}',
        # Specify a caption for the legend
        name='',
        # Specifying the line color
        line=dict(color=color)),
        # Specify line and column numbers
        row=1, col=2)

    # Add an image to the chart
    fig.layout.images = [dict(
        # Passing a link to the image
        source=img_link,
        # Specify the position of the image along the x-axis
        x=0.05,
        # Specify the position of the image along the y-axis
        y=0.5,
        # Setting the size of the chart
        sizex=1,
        sizey=1.6,
        # Setting the position along the x-axis
        xanchor="center",
        # Setting the y-axis position
        yanchor="middle",
        # Place the image under the chart
        layer="below"
    )
    ]

    fig.update_layout(
        # Set the name of the chart
        title=f'<b>{name_one}</b><br><sub>{name_two}</sub>',
        # Setting the background color
        paper_bgcolor="rgb(205, 228, 255)",
        # Setting the chart theme
        template='xgridoff',
        # Passing chart parameters
        polar=dict(
            # Background color
            bgcolor="rgb(205, 228, 255)",
            # Adding a line with numeric divisions
            radialaxis=dict(
                # Displaying the line
                visible=True,
                # Set the range of divisions
                range=[0, 100]
            )
        ),
        # Passing the parameters to the font
        font=dict(
            # Font type
            family='Poppins',
            # Font size
            size=18,
            # Font color
            color='Black'
        )
    )

    # Displaying the graph
    fig.show()

unique_ages = dataset["age"].unique()
unique_ages = sorted(unique_ages)
paces = []
counts = []
for age in unique_ages:
    avg_df = dataset[dataset["age"] == age]["physic"]
    count = avg_df.count()
    mean = avg_df.mean()
    paces.append( mean)
    counts.append(count)
sns.set_style("white")
plt.figure(figsize=(8, 8));
sns.scatterplot(x=unique_ages, y=counts, color="red", size=counts);
sns.despine()
plt.title("Frequency of Ages");
plt.xlabel("Ages");
plt.ylabel("Count");

plt.figure(figsize=(8, 8))
sns.scatterplot(x=unique_ages, y=paces, size=paces, color="magenta");
sns.despine()
plt.title("Age vs Average Physic");
plt.xlabel("Ages");
plt.ylabel("Average Physic");
plt.show()


def Country(x):
    def find_min_max_in(col):
        work = dataset[col].idxmax()
        work_df = pd.DataFrame(dataset.loc[work])
        return work_df

    return dataset[dataset['nationality'] == x][['goalkeeping_handling', 'short_name']].sort_values(
        by=['goalkeeping_handling'], ascending=False)


find_min_max_in('goalkeeping_handling')
Country1 = Country("Republic of Ireland")
print(Country1)
goalkeeper = Country1.iloc[0][1]
print("The goalkeeper is :", goalkeeper)

dataset.drop(dataset[dataset['short_name'] == goalkeeper].index, inplace=True)

