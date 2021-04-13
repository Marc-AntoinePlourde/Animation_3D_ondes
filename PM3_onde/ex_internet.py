import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

# Fixing random state for reproducibility
np.random.seed(19680801)


frames = 5
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


def Gen_RandLine(length, dims=2):
    """
    Create a line using a random walk algorithm

    length is the number of points for the line.
    dims is the number of dimensions the line has.
    """
    lineData = np.empty((dims, length))
    lineData[:, 0] = np.random.rand(dims)
    for index in range(1, length):
        # scaling the random numbers by 0.1 so
        # movement is small compared to position.
        # subtraction by 0.5 is to change the range to [-0.5, 0.5]
        # to allow a line to move backwards.
        step = ((np.random.rand(dims) - 0.5) * 0.1)
        lineData[:, index] = lineData[:, index - 1] + step

    return lineData


def update_lines(t, lines):
    # NOTE: there is no .set_data() for 3 dim data...
    #line.set_data(data[t])
    #line.set_3d_properties(data[t])
    return lines[t]

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)
x = np.linspace(0, a, 15)
y = np.linspace(0, b, 15)
X, Y = np.meshgrid(x, y)
# Fifty lines of random 3-D lines
data = [g(x,y,t) for t in range(frames)]

# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
lines = [ax.plot(x, x, Z)[0] for Z in data]

# Setting the axes properties
ax.set_xlim3d([0.0, a])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, b])
ax.set_ylabel('Y')

ax.set_zlim3d([-6, 6])
ax.set_zlabel('Z')

ax.set_title('3D Test')

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, frames, fargs=(lines,),
                                   interval=50, blit=False)
line_ani.save('internet.gif', writer='imagemagick')
plt.show()