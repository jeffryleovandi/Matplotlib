##Visualisasi Data yang tersimpan pada Pandas Data Frame (bagian 2)
#Import modules
import matplotlib 
import matplotlib.pyplot as plt
import pandas as pd

print(matplotlib.__version__)
print(pd.__version__)

#Line Plot
data = {
    'Tahun': [
        '1958', '1963', '1968', '1973', '1978', '1983', '1988', '1993', '1998',
        '2003', '2008', '2013', '2018'
    ],
    'Populasi': [
        51652500, 53624900, 55213500, 56223000, 56178000, 56315000, 56916000,
        57713000, 58474000, 59636000, 61823000, 64105000, 66436000
    ]
}

df = pd.DataFrame(data)
df

df.plot(x='Tahun', y='Populasi', kind='line')

plt.title('Data Populasi Penduduk')
plt.ylabel('Populasi')
plt.xlabel('Tahun')
plt.show()

#Bar Plot
data = {
    'Negara': ['United States', 'Singapore', 'Germany', 'United Kingdom', 'Japan'],
    'GDP': [62606, 100345, 52559, 45705, 44227]
}

df = pd.DataFrame(data, columns=['Negara', 'GDP'])
df

df.plot(x='Negara', y='GDP', kind='bar')

plt.title('GDP Per Kapita')
plt.ylabel('GDP dalam USD')
plt.xlabel('Negara')
plt.show()

df.plot(x='Negara', y='GDP', kind='barh')

plt.title('GDP Per Kapita')
plt.xlabel('GDP dalam USD')
plt.ylabel('Negara')
plt.show()

df.plot(x='Negara', y='GDP', kind='barh', color='green', legend=False)

plt.title('GDP Per Kapita')
plt.xlabel('GDP dalam USD')
plt.ylabel('Negara')
plt.show()

#Scatter Plot
data = {
    'Negara': ['United States', 'Singapore', 'Germany', 'United Kingdom', 'Japan'],
    'GDP': [52591, 67110, 46426, 38749, 36030],
    'Life_Expectancy': [79.24, 82.84, 80.84, 81.40, 83.62]
}

df = pd.DataFrame(data, columns=['Negara', 'GDP', 'Life_Expectancy'])
df

df.plot(kind='scatter', x='GDP', y='Life_Expectancy', color='red')

plt.title('GDP dan Life Expectancy')
plt.ylabel('Life Expectancy')
plt.xlabel('GDP dan USD')
plt.show()

#Pie Plot
data = {
    'benua': [
        'South America', 'Oceania', 'North America', 'Europe', 'Asia',
        'Antarctica', 'Africa'
    ],
    'populasi':
    [422535000, 38304000, 579024000, 738849000, 4581757408, 1106, 1216130000]
}

df = pd.DataFrame(data)
df

df.plot(kind='pie', y='populasi', figsize=(6, 6))

plt.title('Populasi di tiap Benua')
plt.show()

df = df.set_index('benua')
df

df.plot(kind='pie', y='populasi', figsize=(6, 6))

plt.title('Populasi di tiap Benua')
plt.show()

#Box Plot
data = {
    'benua': [
        'South America', 'Oceania', 'North America', 'Europe', 'Asia',
        'Antarctica', 'Africa'
    ],
    'populasi':
    [422535000, 38304000, 579024000, 738849000, 4581757408, 1106, 1216130000]
}

df = pd.DataFrame(data)
df

df['populasi'].plot(kind='box')

plt.title('Sebaran Populasi')
plt.ylabel('jumlah')
plt.show()