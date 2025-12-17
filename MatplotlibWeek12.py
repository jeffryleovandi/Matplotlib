##Visualisasi Data yang tersimpan pada Pandas Data Frame (bagian 1)
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

print(matplotlib.__version__)
print(pd.__version__)

#Sample Dataset
df = pd.DataFrame({
    'nama': ['cecep', 'karti', 'bejo', 'tejo', 'asep', 'wati', 'amat'],
    'usia': [23, 78, 22, 19, 45, 33, 20],
    'gender': ['L', 'P', 'L', 'L', 'L', 'P', 'L'],
    'propinsi':
    ['jabar', 'jatim', 'jabar', 'jatim', 'jabar', 'jateng', 'jateng'],
    'n_anak': [2, 0, 0, 3, 2, 1, 4],
    'n_pets': [5, 1, 0, 5, 2, 2, 3]
})

df

#Scatter Plot
df.plot(kind='scatter', x='n_anak', y='n_pets', color='red')

plt.title('Scatter Plot')
plt.xlabel('Jumlah Anak')
plt.ylabel('Jumlah Pets')
plt.show()

#Histogram
df[['usia']].plot(kind='hist', bins=[0, 20, 40, 60, 80, 100])

plt.title('Histogram')
plt.xlabel('Usia')
plt.ylabel('Jumlah')
plt.show()

#Line Plot
df.plot(kind='line', x='nama', y='n_anak', color='green')

plt.title('Line Plot')
plt.ylabel('Jumlah Anak')
plt.show()

#Multiple Line Plot
df.plot(kind='line', x='nama', y='n_anak', color='green')
df.plot(kind='line', x='nama', y='n_pets', color='red')

plt.title('Line Plot')
plt.ylabel('Jumlah')
plt.show()

ax = plt.gca()

df.plot(kind='line', x='nama', y='n_anak', color='green', ax=ax)
df.plot(kind='line', x='nama', y='n_pets', color='red', ax=ax)

plt.title('Line Plot')
plt.ylabel('Jumlah')
plt.show()

#Bar Plot
df.plot(kind='bar', x='nama', y='usia')

plt.title('Bar Plot')
plt.ylabel('Usia')
plt.show()

df.groupby('propinsi')['nama'].count().plot(kind='bar')

plt.title('Bar Plot')
plt.ylabel('Jumlah')
plt.show()

#Stacked bar plot dengan dua level group by
df.groupby(['propinsi', 'gender']).size().unstack().plot(kind='bar',
                                                         stacked=True)

plt.title('Bar Plot')
plt.ylabel('Jumlah')
plt.show()

df.groupby(['gender', 'propinsi']).size().unstack().plot(kind='bar',
                                                         stacked=True)

plt.title('Stacked Bar Plot')
plt.ylabel('Jumlah')
plt.show()