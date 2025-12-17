##Pengenalan pyplot
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)
#3.9.2 -> versi matplotlib
#1.26.4 -> versi numpy

#Membuat plotting sederhana
plt.plot([2, 5, 7, 11])
plt.ylabel('sumbu y')
plt.show()

plt.plot([2, 3, 4, 7], [5, 4, 2, 16])
plt.show()

#Pengaturan Format pada plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'go')
plt.axis([0, 6, 0, 20])
plt.show()

#Multi plot dalam satu pemanggilan fungsi plot()
t = np.arange(0., 5., 0.2)
t
plt.plot(t, t, 'r--')
plt.plot(t, t**2, 'bs')
plt.plot(t, t**3, 'g^')
plt.show()


plt.plot(t, t, 'r--', 
         t, t**2, 'bs', 
         t, t**3, 'g^')
plt.show()

#Plotting dengan keywords
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
data

plt.scatter('a', 'b', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

#Plotting untuk tipe data categorical
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.plot(names, values)
plt.show()

plt.scatter(names, values)
plt.show()

plt.bar(names, values)
plt.show()