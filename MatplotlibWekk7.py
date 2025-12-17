##3D Plotting
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#3D Axes
fig = plt.figure()
ax = plt.axes(projection='3d')

plt.show()

#3D Line Plot
z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot(x, y, z, color='red')

ax.set(title='Contoh 3D Line Plot',
       xlabel='Sumbu X',
       ylabel='Sumbu Y',
       zlabel='Sumbu Z')

plt.show()

#3D Scatter Plot
z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter(x, y, z, color='green')

ax.set(title='Contoh 3D Scatter Plot',
       xlabel='Sumbu X',
       ylabel='Sumbu Y',
       zlabel='Sumbu Z')

plt.show()

##Contour Plot
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Sample dataset
n = np.linspace(-3.0, 3.0, 100)

x, y = np.meshgrid(n, n)
z = np.sqrt(x**2 + y**2)

print(x.shape)
print(y.shape)
print(z.shape)

#Contour Plot
plt.contour(x, y, z)
plt.colorbar()

plt.title('Contour Plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.show()

#Filled Contour Plot
plt.contourf(x, y, z)
plt.colorbar()

plt.title('Filled Contour Plot')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.show()

##3D Area Plotting
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Sample dataset
n = np.linspace(-3.0, 3.0, 100)

x, y = np.meshgrid(n, n)
z = np.sqrt(x**2 + y**2)

print(x.shape)
print(y.shape)
print(z.shape)

#3D Wireframe
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_wireframe(x, y, z, color='orange')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D Wireframe')

plt.show()

#3D Surface Plot
fig = plt.figure()
ax = plt.axes(projection='3d')

# ax.plot_surface(x, y, z, color='orange')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D Surface Plot')

plt.show()