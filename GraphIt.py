import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(211)


def animate(i):
    file1 = open("CSC495Data.txt", "r")
    data_file = file1.read()

    traffic = data_file.split('\n')

    xs = []
    ys = []
    n = 0
    for info in traffic:
        if len(info) > 1:
            n = n + 5
            ys.append(float(info))
            xs.append(n)

    ax1.clear()
    ax1.plot(xs, ys)
    file1.close()


anim = animation.FuncAnimation(fig, animate, interval=10000)
plt.show()
