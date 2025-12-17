##Pengaturan Figure Layouts dengan GridSpec
#Import modules
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

print(matplotlib.__version__)
print(np.__version__)

#Simple 2x2 layout dengan subplots
siswa = ['Cecep', 'Joko', 'Wati', 'Ani']
uas = [68, 83, 96, 72]

fig, axes = plt.subplots(ncols=2, nrows=2, constrained_layout=True)

axes[0][0].bar(siswa, uas)
axes[0][1].pie(uas, labels=siswa)
axes[1][0].pie(uas, labels=siswa, explode=[0, 0, 0, 0.2])
axes[1][1].barh(siswa, uas)

plt.show()

#Simple 2x2 layout dengan GridSpec
fig = plt.figure(constrained_layout=True)

gs = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])

ax1.bar(siswa, uas)
ax2.pie(uas, labels=siswa)
ax3.pie(uas, labels=siswa, explode=[0, 0, 0, 0.2])
ax4.barh(siswa, uas)

plt.show()

fig = plt.figure(constrained_layout=True)

gs = fig.add_gridspec(ncols=2, nrows=2)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])

ax1.bar(siswa, uas)
ax2.pie(uas, labels=siswa)
ax3.pie(uas, labels=siswa, explode=[0, 0, 0, 0.2])
ax4.barh(siswa, uas)

plt.show()

#Rows Span dan Cols Span dengan GridSpec
fig = plt.figure(constrained_layout=True)

gs = fig.add_gridspec(ncols=2, nrows=2)

ax1 = fig.add_subplot(gs[0, :])
# ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])

ax1.bar(siswa, uas)
# # ax2.pie(uas, labels=siswa)
ax3.pie(uas, labels=siswa, explode=[0, 0, 0, 0.2])
ax4.barh(siswa, uas)

plt.show()

fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(ncols=3, nrows=3)

ax1 = fig.add_subplot(gs[0, :])
ax1.set_title('gs[0, :]')

ax2 = fig.add_subplot(gs[1, :-1])
ax2.set_title('gs[1, :-1]')
ax2.barh(siswa, uas)

ax3 = fig.add_subplot(gs[1:, -1])
ax3.set_title('gs[1:, -1]')
ax3.bar(siswa, uas)

ax4 = fig.add_subplot(gs[-1, 0])
ax4.set_title('gs[-1, 0]')

ax5 = fig.add_subplot(gs[-1, -2])
ax5.set_title('gs[-1, -2]')

plt.show()