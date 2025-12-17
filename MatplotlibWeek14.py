##Visualisasi Data yang tersimpan pada Pandas Data Frame (bagian 3)
#Import modules
import matplotlib 
import matplotlib.pyplot as plt
import pandas as pd

print(matplotlib.__version__)
print(pd.__version__)

#Sample Dataset
df = pd.read_csv('./dataset/2020.csv')
df.head()

df.rename(columns={
    'Country name': 'Country',
    'Perceptions of corruption': 'Corruption',
    'Freedom to make life choices': 'Freedom'
},
          inplace=True)
df.columns

#Bar plot
df[:5].plot(x='Country',
            y=['Corruption', 'Freedom', 'Generosity', 'Social support'],
            kind='bar')


plt.title('Contoh Bar Plot')
plt.ylabel('Nilai')
plt.show()

#Line plot
df[:5].plot(x='Country',
            y=['Corruption', 'Freedom', 'Generosity', 'Social support'],
            kind='line')

plt.title('Contoh Line Plot')
plt.ylabel('Nilai')
plt.show()

#Box plot
df.plot(y=['Corruption', 'Freedom', 'Generosity', 'Social support'],
        kind='box')

plt.title('Contoh Box Plot')
plt.xlabel('Parameter')
plt.ylabel('Nilai')
plt.show()

#Scatter plot
df.plot(x='Corruption', y='Freedom', kind='scatter')

plt.xlim((0,1))
plt.ylim((0,1))

plt.title('Contoh Scatter Plot')
plt.show()

#Histogram
df.plot(x='Country', y='Corruption', kind='hist', bins=10)

plt.title('Contoh Histogram')
plt.xlabel('Nilai')
plt.show()

df.plot(x='Country',
        y=['Corruption', 'Freedom', 'Generosity', 'Social support'],
        kind='hist',
        subplots=True,
        layout=(2, 2))

plt.suptitle('Contoh Subplots')
plt.tight_layout()
plt.show()