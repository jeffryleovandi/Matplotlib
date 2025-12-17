##Multiple Subplots
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Simple Line Plot
x = np.arange(0.0, 2.0, 0.01)
x

s = np.sin(2 * np.pi * x)
s

fig, ax = plt.subplots() # OO Style

ax.plot(x, s)
ax.set(xlabel='nilai x', 
       ylabel='nilai sin(x)',
       title='Visualisasi nilai sin')
ax.grid()

plt.show()

#Multiple Subplots
x1 = np.linspace(0.0, 5.0, 100)
x2 = np.linspace(0.0, 2.0, 100)

y1 = np.cos(2 * np.pi * x1) 
y2 = np.cos(2 * np.pi * x2)
x1

#Multiple Subplots dengan OO Style
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Multiple Subplots')

ax1.plot(x1, y1, 'ro-')
ax1.set_ylabel('Nilai $cos(x_1)$')

ax2.plot(x2, y2, 'g.-')
ax2.set_ylabel('Nilai $cos(x_2)$')

ax2.set_xlabel('Nilai x')

plt.show()

#Multiple Subplots dengan pyplot Style
plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'ro-')
plt.title('Multiple Subplots')
plt.ylabel('Nilai $cos(x_1)$')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'g.-')
plt.ylabel('Nilai $cos(x_2)$')
plt.xlabel('Nilai $x$')

plt.show()

##Histogram
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Sample Data
mu, sigma = 100, 15 # nilai mean dan nilai standard deviation

x = mu + sigma * np.random.randn(10000) # normal distribution
x

x.shape
#(10000,)

#Histogram dengan pyplot Style
plt.hist(x, 
         bins=50, 
         facecolor='g', 
         alpha=0.50)

plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Contoh Histogram')

plt.text(45, 500, '$\mu=100,\ \sigma=15$')
plt.grid()

plt.show()

#Histogram dengan OO Style
fig, ax = plt.subplots()

ax.hist(x, 
        bins=50, 
        facecolor='b', 
        alpha=0.25)

ax.set_xlabel('Sumbu X')
ax.set_ylabel('Sumbu Y')
ax.set_title('Contoh Histogram')

ax.text(45, 500, '$\mu=100,\ \sigma=15$')
ax.grid()

plt.show()