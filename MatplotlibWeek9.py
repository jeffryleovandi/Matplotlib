##Matplotlib Customisation: Style Sheets
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Predefined Styles
plt.style.available
plt.style.use('ggplot')
x = np.linspace(1, 10, 15)

plt.plot(x, x, 'bs-', label='lin')
plt.plot(x, np.log(x), 'ro-', label='log')

plt.legend()
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Contoh Plot')

plt.show()

#Membuat Style sendiri
plt.style.use('./style_ku.mplstyle')
x = np.linspace(1, 10, 15)

plt.plot(x, x, 'bs-', label='lin')
plt.plot(x, np.log(x), 'ro-', label='log')

plt.legend()
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Contoh Plot')

plt.show()

#Menerapkan multiple style
## DEPRECATED
# plt.style.use(['seaborn', 'dark_background'])
x = np.linspace(1, 10, 15)

plt.plot(x, x, 'bs-', label='lin')
plt.plot(x, np.log(x), 'ro-', label='log')

plt.legend()
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Contoh Plot')

plt.show()

#Menerapkan temporary styling
plt.style.use('ggplot')

plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
plt.show()

with plt.style.context('dark_background'):
    plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')

plt.show()

plt.plot(np.sin(np.linspace(0, 2 * np.pi)), 'r-o')
plt.show()