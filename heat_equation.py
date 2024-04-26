import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


Nx = 100
Ny = 80
Nt = 10000


u = np.zeros((Nx, Ny, Nt))

density = 1
specific_heat = 1
conductivity = 1
alfa = conductivity/(density*specific_heat)
alfa = 0.22

dx = 1/Nx
dy = 1/Ny
dt = 1/Nt
delta  = 0.05


# Initialbetingelser
#Set all values to 23.8
u[:, :, :] = 23.8
u[0, :, :] = 77
for n in range(0, Nt-1):
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            u[i, j, n+1] = u[i, j, n] + alfa*delta*(u[i+1, j, n] - 2*u[i, j, n] + u[i-1, j, n]) + alfa*delta*(u[i, j+1, n] - 2*u[i, j, n] + u[i, j-1, n])


#animate u

def plot(i):
    plt.clf()
    plt.imshow(u[:, :, i], cmap='plasma', interpolation='nearest')
    #change colorbar color ranging from red(hot) to blue(cold)
    time = int(i*dt)
    plt.title('Temperature at time: %d' % i)
    plt.xlabel('x')
    plt.ylabel('y')


    plt.colorbar()
    plt.clim(15, 80)
    #lock the colorbar
    
    


fig = plt.figure()
ani = animation.FuncAnimation(fig, plot, frames=Nt, interval=100)
plt.show()
