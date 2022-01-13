d = grouped_data.get_group(("Real Madrid", 20801))
sns.lineplot(x=d.year, y=d['pace'])
plt.xticks(d.year)
plt.title("Ronaldo's pace over the years when he was in Real Madrid")
