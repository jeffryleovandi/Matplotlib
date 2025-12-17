##Plot Lifecycle
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Sample dataset
data = {'Item A': 109438,
        'Item B': 103569,
        'Item C': 112214,
        'Item D': 112591,
        'Item E': 100934,
        'Item F': 103660,
        'Item G': 137351,
        'Item H': 123381,
        'Item I': 135841,
        'Item J': 104437}

data

items = tuple(data.keys())
items

count = tuple(data.values())
count

#Simple Plot
fig, ax = plt.subplots()

ax.barh(items, count)

plt.show()

#Pengaturan Style
plt.style.available

plt.style.use('bmh')

fig, ax = plt.subplots()
ax.barh(items, count)
plt.show()

#Pengaturan Tick Label
fig, ax = plt.subplots()
ax.barh(items, count)

labels = ax.get_xticklabels()

# set properties
plt.setp(labels,
         rotation=45,
         horizontalalignment='right')

plt.show()

#Pengaturan Format pada Ticker
from matplotlib.ticker import FuncFormatter
def ribuan(x, pos):
    return f'{int(x/1000)}K'
fig, ax = plt.subplots()
ax.barh(items, count)

formatter = FuncFormatter(ribuan)
ax.xaxis.set_major_formatter(formatter)

ax.set(title='Contoh Plot', 
       xlabel='Jumlah', 
       ylabel='Items')

plt.show()

#Pengaturan Label pada Sumbu (axis) dan Judul (title)
fig, ax = plt.subplots()
ax.barh(items, count)

ax.set(title='Contoh Plot', 
       xlabel='Jumlah', 
       ylabel='Items')

plt.show()

#Penambahan Garis (vertical/horisontal line) pada Plot
fig, ax = plt.subplots()
ax.barh(items, count)

ax.axvline(np.mean(count), 
           ls='--', 
           color='r')

ax.set(title='Contoh Plot', 
       xlabel='Jumlah', 
       ylabel='Items')

plt.show()

#Menyimpan Hasil Plot ke dalam suatu File
fig.canvas.get_supported_filetypes()

fig, ax = plt.subplots()
ax.barh(items, count)

ax.axvline(np.mean(count),
           ls='--',
           color='r')

ax.set(title='Contoh Plot',
       xlabel='Jumlah',
       ylabel='Items')

fig.savefig('coba.png',
            transparent=True,
            dpi=80)