import pandas as pd

df = pd.read_csv('data/transactions.csv', index_col=0)

ok = df[df['STATUS'] == 'OK']

print('Три самых крупных платежа:')
print(ok.sort_values('SUM', ascending=False).head(3))

umbrella = ok[ok['CONTRACTOR'] == 'Umbrella, Inc']
print('Сумма платежей Umbrella, Inc:', umbrella['SUM'].sum())
