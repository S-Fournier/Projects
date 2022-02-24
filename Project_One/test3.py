import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(0, 20))
dot, = ax.plot([], [], 'bo', ms=1)

# initialization function: plot the background of each frame
def init():
    dot.set_data([], [])
    return dot,

# animation function.  This is called sequentially
def animate(i):
    x = np.random.uniform(0,20,10)
    y = np.random.uniform(0,20,10)
    dot.set_data(x, y)
    return dot,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=600, interval=600, blit=True)

plt.show()