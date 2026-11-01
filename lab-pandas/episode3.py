import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('data/students/students_info.xlsx')
results = pd.read_html('data/students/results_ejudge.html')[0]

df = students.merge(results, left_on='login', right_on='User')

by_faculty = df.groupby('group_faculty')['Solved'].mean()
by_out = df.groupby('group_out')['Solved'].mean()
print(by_faculty)
print(by_out)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

by_faculty.plot(kind='bar', ax=axes[0], rot=0)
axes[0].set_title('По факультетским группам')
axes[0].set_ylabel('Среднее число решённых задач')

by_out.plot(kind='bar', ax=axes[1], rot=0)
axes[1].set_title('По группам по информатике')

plt.tight_layout()
plt.show()

good = df[(df['G'] > 10) | (df['H'] > 10)]
print(good[['login', 'group_faculty', 'group_out', 'G', 'H']])
print('Факультетские группы:', good['group_faculty'].unique())
print('Группы по информатике:', good['group_out'].unique())
