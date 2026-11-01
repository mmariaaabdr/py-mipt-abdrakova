import pandas as pd

transactions = pd.read_csv('data/transactions.csv', index_col=0)
flights = pd.read_csv('data/flights.csv', index_col=0)
students = pd.read_excel('data/students/students_info.xlsx')
results = pd.read_html('data/students/results_ejudge.html')[0]

print(transactions[transactions['SUM'] > 1000])

print(flights.index.is_unique)

print(students[students['login'].isna()])

extra = results[~results['User'].isin(students['login'])]
print(extra[['User', 'Score']])

print(students['group_faculty'].unique())
print(students['group_out'].unique())

print(results['Place'].unique())
print(results[['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']].max())
