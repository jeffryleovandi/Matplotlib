##Bar Plot / Bar Chart
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Simple Bar Plot
data = [25, 45, 55, 125, 225]
kategori = ['A', 'B', 'C', 'D', 'E']
plt.bar(kategori, data)
plt.grid()

plt.xlabel('Kategori')
plt.ylabel('Jumlah')
plt.title('Contoh Bar Plot')

plt.show()

#Pengaturan Grid dan Color
data = [25, 45, 55, 125, 225]
kategori = ['A', 'B', 'C', 'D', 'E']
plt.bar(kategori, 
        data, 
        color='red', 
        alpha=0.25)

plt.grid(linestyle='--', 
         linewidth=2, 
         axis='y', # pilihan: x, y, both
         alpha=0.50)

plt.xlabel('Kategori')
plt.ylabel('Jumlah')
plt.title('Contoh Bar Plot')

plt.show()

#Horisontal Bar Plot
data = [25, 45, 55, 125, 225]
kategori = ['A', 'B', 'C', 'D', 'E']
plt.barh(kategori, data)
# plt.barh(kategori[::-1], data[::-1])

plt.grid(linestyle='--', 
         linewidth=1, 
         axis='x',
         alpha=0.75)

plt.xlabel('Jumlah')
plt.ylabel('Kategori')
plt.title('Contoh Horisontal Bar Plot')

plt.show()

#Stacked Bar Plot
data1 = [25, 85, 75, 40, 60]
data2 = [40, 35, 20, 55, 10]
kategori = ['A', 'B', 'C', 'D', 'E']
plt.bar(kategori, data1, label='Data 1')
# plt.bar(kategori, data2, label='Data 2')
plt.bar(kategori, data2, label='Data 2', bottom=data1)

plt.legend()

plt.grid(linestyle='--', 
         linewidth=1, 
         axis='y',
         alpha=0.75)

plt.xlabel('Kategori')
plt.ylabel('Jumlah')
plt.title('Contoh Stacked Bar Plot')

plt.show()

#Grouped Bar Plot
data1 = [25,85, 75, 40, 60]
data2 = [40, 35, 20, 55, 10]
kategori = ['A', 'B', 'C', 'D', 'E']

x = np.arange(len(kategori))
x

width = 0.35

plt.bar(x-width/2, data1, width, label='Data 1')
plt.bar(x+width/2, data2, width, label='Data 2')

plt.xticks(x, kategori)

plt.grid(linestyle='--', 
         linewidth=1, 
         axis='y',
         alpha=0.75)

plt.xlabel('Kategori')
plt.ylabel('Jumlah')
plt.title('Contoh Grouped Bar Plot')

plt.legend()
plt.show()

##Pie Plot / Pie Chart
#Import modules
import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.__version__)
#3.9.2 -> versi matplotlib

#Simple Pie Plot
kategori = ['A', 'B', 'C', 'D', 'E']
data = [215, 130, 245, 210, 225]
plt.pie(data, 
        labels=kategori,
        autopct='%1.1f%%',
        startangle=90)

plt.title('Contoh Pie Plot')

plt.show()

#Pengaturan Legend dan Color
kategori = ['A', 'B', 'C', 'D', 'E']
data = [215, 130, 245, 210, 225]
warna = ['pink', 'cyan', '#e03364', 'yellowgreen', 'skyblue']
plt.pie(data, 
        labels=kategori,
        colors=warna,
        autopct='%1.1f%%',
        startangle=90)

plt.legend()
plt.title('Contoh Pie Plot')

plt.show()

#Exploded Pie Plot
kategori = ['A', 'B', 'C', 'D', 'E']
data = [215, 130, 245, 210, 225]
warna = ['pink', 'cyan', '#e03364', 'yellowgreen', 'skyblue']
explode_var = [0., 0., 0.2, 0., 0.08]
plt.pie(data, 
        labels=kategori,
        colors=warna,
        explode=explode_var,
        autopct='%1.1f%%',
        startangle=90)

plt.title('Contoh Exploded Pie Plot')

plt.show()

##Table Plot / Table Chart
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Sample Data
data_uas=[
    ['Bejo', 70],
    ['Tejo', 83],
    ['Cecep', 62],
    ['Wati', 74],
    ['Karti', 71]
]
data_uas
#[['Bejo', 70], ['Tejo', 83], ['Cecep', 62], ['Wati', 74], ['Karti', 71]]

#Table Plot dengan OO Style
fig, ax = plt.subplots()

table = plt.table(cellText=data_uas, 
                  loc='center')

table.set_fontsize(14)
table.scale(1, 4) # ukuran kolom, baris

ax.axis(False)

plt.show()

#Table Plot dengan pyplot Style
table = plt.table(cellText=data_uas, 
                  loc='center')

table.set_fontsize(14)
table.scale(1, 4) # ukuran kolom, baris

ax = plt.gca()
ax.axis(False)

plt.show()