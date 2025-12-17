##Box Plot / Box Chart
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Sample Dataset
np.random.seed(2)
data = np.random.normal(loc=100, scale=10, size=200)
data

#Simple Box Plot
## DEPRECATED
# plt.boxplot(data, labels=['Data'])

# plt.title('Simple Box Plot')
# plt.xlabel('Sumbu X')
# plt.ylabel('Sumbu Y')

# plt.grid()
# plt.show()
plt.boxplot(data, tick_labels=['Data'])

plt.title('Simple Box Plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.grid()
plt.show()

#Notched Box Plot
plt.boxplot(data, tick_labels=['Data'], notch=True)

plt.title('Notched Box Plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.show()

#Pengaturan marker untuk outlier
plt.boxplot(data, 
            tick_labels=['Data'],
            showfliers=True, 
            flierprops={'markerfacecolor':'r', 'marker':'s'})

plt.title('Pengaturan Marker')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.show()

#Horisontal Box Plot
plt.boxplot(data, tick_labels=['Data'], vert=False)

plt.title('Horisontal Box Plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.show()

#Multiple Box Plot
np.random.seed(10)
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(80, 30, 200)
data3 = np.random.normal(90, 20, 200)
data4 = np.random.normal(70, 25, 200)

data = [data1, data2, data3, data4]
labels = ['Data 1', 'Data 2', 'Data 3', 'Data 4']
## DEPRECATED
# plt.boxplot(data, labels=labels)

# plt.title('Multiple Box Plot')
# plt.xlabel('Sumbu X')
# plt.ylabel('Sumbu Y')

# plt.show()
plt.boxplot(data, tick_labels=labels)

plt.title('Multiple Box Plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.show()

##Violin Plot / Violin Chart
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Sample Dataset
np.random.seed(2)
data = np.random.normal(loc=100, scale=10, size=200)
data

#Simple Violin Plot
plt.violinplot(data)

plt.title('Simple Violin Plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.show()

#Pengaturan pada Violin Plot
plt.violinplot(data,
               showextrema=True,
               showmeans=False,
               showmedians=False,
               quantiles=[0.25, 0.5, 0.75])

plt.title('Violin Plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.show()

#Horisontal Violin Plot
plt.violinplot(data, vert=False)

plt.title('Horisontal Violin Plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.show()

#Multiple Violin Plot
np.random.seed(10)
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(80, 30, 200)
data3 = np.random.normal(90, 20, 200)
data4 = np.random.normal(70, 25, 200)

data = [data1, data2, data3, data4]
plt.violinplot(data)

plt.title('Multiple Violin Plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.show()

##Twin Axes
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Kasus Twin Axes 1
x = np.linspace(1, 10, 25)
x

fig, ax1 = plt.subplots()

ax1.plot(x, np.exp(x), 'bs-', label='exp')
ax1.set_xlabel('Sumbu X')
ax1.set_ylabel('exp')

ax2 = ax1.twinx()
ax2.plot(x, np.log(x), 'ro-', label='log')
ax2.set_ylabel('log')

fig.suptitle('Contoh Twin Axes')
fig.legend(loc='lower left')

plt.show()

#Kasus Twin Axes 2
x = np.random.randint(16, 40, size=30)
x

def C2F(celsius=0):
    return (celsius * 1.8) + 32

def konversi_sumbu(ax1): 
    y1, y2 = ax1.get_ylim() 
    ax2.set_ylim(C2F(y1), C2F(y2)) 
    ax2.figure.canvas.draw() 

fig, ax1 = plt.subplots() 
ax2 = ax1.twinx() 

ax1.callbacks.connect('ylim_changed', konversi_sumbu) 
ax1.plot(x) 

ax1.set_xlabel('Hari')
ax1.set_ylabel('Celsius') 
ax2.set_ylabel('Fahrenheit') 

fig.suptitle('Temperatur Udara') 
plt.show() 