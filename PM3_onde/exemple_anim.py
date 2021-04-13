import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import FuncAnimation


n = 1
m = 2
a = 2
b = 2
c = 2
s = 50
pi = 3.141592653589793238462

def g(x, y, t):
    k = 0
    for n in range(1, s+1):
        for m in range(1, s+1):
            P = (32*(1-np.cos(pi*(m-(1/2))))*(1-np.cos(pi*(n-(1/2)))))/(pi**2*(2*m-1)*(2*n-1))
            omega = pi / 2*np.sqrt((n-1/2)**2+(m-1/2)**2)
            k += np.sin((n- 1 / 2)*np.pi*x / 2)*np.sin((m - 1 / 2)*np.pi*y/2)*P*np.cos(c *omega*t)
    return k


fig = plt.figure()
ax = plt.axes(projection='3d')
x = np.linspace(0, a, 15)
y = np.linspace(0, b, 15)
X, Y = np.meshgrid(x, y)
Z = g(X, Y, 0)
ln = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

def init():
    ax.set_zlim(-6, 6)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim(0, a)
    ax.set_ylim(0, b)
    return ln,

def update(frame):
    global ln
    ln.remove()
    t = frame*0.01
    x = np.linspace(0, a, 150)
    y = np.linspace(0, b, 150)
    X, Y = np.meshgrid(x, y)
    Z = g(X, Y, t)
    ln = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    return ln,

ani = FuncAnimation(fig, update, frames=np.arange(0, 500),
                    init_func=init, blit=True)

ani.save(f'jaimelespag.gif', writer='imagemagick')
#plt.show()