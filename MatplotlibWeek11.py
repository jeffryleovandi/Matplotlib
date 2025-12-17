##Animasi pada Matplotlib
#Import modules
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython import display
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Review Figure
fig = plt.figure()
plt.xlim((0, 8))
plt.ylim((-4, 2))

print(plt.plot([]))

#Animasi pada Matplotlib
fig = plt.figure()
plt.xlim((0, 4))
plt.ylim((-2, 2))

line = plt.plot([])[0]


def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,


anim = FuncAnimation(fig, animate, frames=200, interval=50)

video = anim.to_html5_video()
html = display.HTML(video)
display.display(html)

plt.close()