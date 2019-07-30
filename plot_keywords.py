import matplotlib.pyplot as plt
import pandas as pd

movies = pd.read_csv('improved_import_movies.csv')

grouped = movies.groupby('keyword')
group_of_groups = []
for group in grouped.groups:
    group_of_groups.append(grouped.get_group(group))

fig, ax = plt.subplots(5, 11)

for idx, axis in enumerate(ax.flat):
    axis.scatter(group_of_groups[idx]['corrected_budget'], group_of_groups[idx]['gross'])
    axis.set_xlabel('budget')
    axis.set_ylabel('gross')
    axis.set_title(group_of_groups[idx]['keyword'].any())

plt.show()
