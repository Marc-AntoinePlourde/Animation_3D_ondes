import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib


global t
n = 1
m = 2
a = 2
b = 2
c = 2
s = 50
pi = 3.141592653589793238462


def f(x, y, t):
    P = (32*(1-np.cos(pi*(m-(1/2))))*(1-np.cos(pi*(n-(1/2)))))/(pi**2*(2*m-1)*(2*n-1))
    omega = pi / 2*np.sqrt((n-1/2)**2+(m-1/2)**2)
    return np.sin((n- 1 / 2)*np.pi*x / 2)*np.sin((m - 1 / 2)*np.pi*y/2)*P*np.cos(c *omega*t)



def g(x, y, t):
    k = 0
    for n in range(1, s+1):
        for m in range(1, s+1):
            P = (32*(1-np.cos(pi*(m-(1/2))))*(1-np.cos(pi*(n-(1/2)))))/(pi**2*(2*m-1)*(2*n-1))
            omega = pi / 2*np.sqrt((n-1/2)**2+(m-1/2)**2)
            k += np.sin((n- 1 / 2)*np.pi*x / 2)*np.sin((m - 1 / 2)*np.pi*y/2)*P*np.cos(c *omega*t)
    return k


for i in reversed(range(50)):
    t = i*0.05
    x = np.linspace(0, a, 150)
    y = np.linspace(0, b, 150)
    X, Y = np.meshgrid(x, y)
    Z = g(X, Y, t)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_zlim(-6, 6)
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')



#def h(x, y, t, n, m):
#    P = (32*(1-np.cos(pi*(m-(1/2))))*(1-np.cos(pi*(n-(1/2)))))/(pi**2*(2*m-1)*(2*n-1))
#    omega = pi / 2*np.sqrt((n-1/2)**2+(m-1/2)**2)
#    return np.sin((n- 1 / 2)*np.pi*x / 2)*np.sin((m - 1 / 2)*np.pi*y/2)*P*np.cos(c *omega*t)
#
#t = i*0.05
#x = np.linspace(0, a, 150)
#y = np.linspace(0, b, 150)
#X, Y = np.meshgrid(x, y)
#Z = g(X, Y, t)
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.set_zlim(-6, 6)
#ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')

#for n in range(1, 3):
#    for m in range(1, 3):
#        t = 0
#        x = np.linspace(0, a, 150)
#        y = np.linspace(0, b, 150)
#        X, Y = np.meshgrid(x, y)
#        Z = h(X, Y, t, n, m)
#        fig = plt.figure()
#        ax = plt.axes(projection='3d')
#        ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
#        ax.set_title(f'mode {n}, {m}')
#        ax.set_xlabel('x')
#        ax.set_ylabel('y')
#        ax.set_zlabel('z')


N = 30 # Meshsize
fps = 10 # frame per sec
durée = 5 # frame number of the animation
frn = fps*durée
x = np.linspace(0, 2, N+1)
x, y = np.meshgrid(x, x)
zarray = np.zeros((N+1, N+1, durée*fps))


for i in range(fps*durée):
    zarray[:,:,i] = g(x,y,i)


def update_plot(frame_number, zarray, plot):
    #global t
    #t = frame_number / fps
    plot[0].remove()
    plot[0] = ax.plot_surface(x, y, zarray[:,:,frame_number], cmap="magma")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plot = [ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')]
#ax.set_zlim(0,1.1)
ani = animation.FuncAnimation(fig, update_plot, frn, fargs=(zarray, plot), interval=1000/fps)

fn = 'plot_surface_animation_funcanimation'
ani.save('plot_surface_animation_funcanimation.gif', fps=fps) #,writer='ffmpeg',fps=fps)
#ani.save(fn+'.gif') #,writer='imagemagick',fps=fps)


#import subprocess
#cmd = 'magick convert %s.gif -fuzz 5%% -layers Optimize %s_r.gif'%(fn,fn)
#subprocess.check_output(cmd)

