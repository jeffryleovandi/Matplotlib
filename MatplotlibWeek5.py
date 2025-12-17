##Scatter Plot / Scatter Chart
#Import modules
import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.__version__)

#Simple Scatter Plot
x = [2,4,6,8,10,11,11.5,11.7]
y = [1,1.5,2,2.5,3,3.5,4,4.5]
plt.scatter(x, y, label='Data 1', color='r')

plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Contoh Scatter Plot')

plt.legend()

plt.show()

#Multiple Scatter Plot
x1 = [2,4,6,8,10,11,11.5,11.7]
y1 = [1,1.5,2,2.5,3,3.5,4,4.5]

x2 = [8,8.5,9,9.5,10,10.5,11]
y2 = [3,3.5,3.7,4,4.5,5,5.2]
plt.scatter(x1, y1, label='Data 1', color='r')
plt.scatter(x2, y2, label='Data 2', color='b')

plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Multiple Scatter Plot')

plt.legend()
plt.show()

#Pengaturan Marker
x1 = [2,4,6,8,10,11,11.5,11.7]
y1 = [1,1.5,2,2.5,3,3.5,4,4.5]

x2 = [8,8.5,9,9.5,10,10.5,11]
y2 = [3,3.5,3.7,4,4.5,5,5.2]
plt.scatter(x1, y1, 
            color='cyan',  
            linewidths=2,  
            marker='s',  
            edgecolor='black',  
            s=400) 
  
plt.scatter(x2, y2, 
            color='yellow', 
            linewidths=1, 
            marker='^',  
            edgecolor='blue',  
            s=200) 

plt.show()

#Scatter Plot untuk data multi dimensi
from sklearn.datasets import load_iris
iris = load_iris()
features = iris['data'].T
iris.keys()
iris['data']
iris['feature_names']
features = iris['data'].T
features
iris['target']
iris['target_names']

plt.scatter(features[0], features[1], 
            alpha=0.2,
            s=100*features[3], 
            c=iris['target'], 
            cmap='viridis')

plt.xlabel(iris['feature_names'][0])
plt.ylabel(iris['feature_names'][1])
plt.title('Iris Dataset')

plt.colorbar()

plt.show()

##Matplotlib Style
#Import modules
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Fungsi plotting
def gambar_barplot():
    data1 = [25,85, 75, 40, 60]
    data2 = [40, 35, 20, 55, 10]
    kategori = ['A', 'B', 'C', 'D', 'E']

    x = np.arange(len(kategori))
    
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
gambar_barplot()

#Matplotlib Style
plt.style.available
style.use('ggplot')
gambar_barplot()