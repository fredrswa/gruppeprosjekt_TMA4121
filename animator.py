import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



Nx = 0
Ny = 0
Nt = 0

with open('heat_equation.txt', 'r') as file:
    Nx = int(file.readline())
    Ny = int(file.readline())
    Nt = int(file.readline())
    u = np.zeros((Nx, Ny, Nt))
    for n in range(0, Nt):
        for i in range(0, Nx):
            for j in range(0, Ny):
                u[i, j, n] = float(file.readline())

def plot(i):
    plt.clf()
    plt.imshow(u[:, :, i], cmap='plasma', interpolation='nearest')
    plt.title('Temperature at time: %d' % i)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar()
    plt.clim(15, 40)
    
    
fig = plt.figure()
ani = animation.FuncAnimation(fig, plot, frames=Nt, interval=0.1, repeat=False)
#ani.save('heat_equation.gif', writer='Pillow', fps=10)
plt.show()
#clear heat_equation.txt
open('heat_equation.txt', 'w').close()