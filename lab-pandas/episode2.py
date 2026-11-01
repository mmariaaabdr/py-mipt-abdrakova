import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/flights.csv', index_col=0)

groups = df.groupby('CARGO')
result = pd.DataFrame()
result['flights'] = groups['CARGO'].count()
result['price'] = groups['PRICE'].sum()
result['weight'] = groups['WEIGHT'].sum()
print(result)

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

result['flights'].plot(kind='bar', ax=axes[0], rot=0)
axes[0].set_title('Число рейсов')

result['price'].plot(kind='bar', ax=axes[1], rot=0)
axes[1].set_title('Стоимость груза')

result['weight'].plot(kind='bar', ax=axes[2], rot=0)
axes[2].set_title('Масса груза')

plt.tight_layout()
plt.show()
