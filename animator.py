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
ani.save('figures/heat_equation.gif', writer='Pillow', fps=10)
plt.show()


#Experimential results
t = np.linspace(0, 380, 20)
T_ob = np.array([23.8, 24.7,25.9,26.5,27.6,28,28.5,29,28.8,30.6,30.2,30.2,30.2,30.2,30.5,30.4,30.4,30.5,30.5,30.6])
T_nm = np.zeros(20)
n = 0
x = 3
y = 2
for time in range(0,np.size(u[x][y]),np.size(u[x][y])//20):
    T_nm[n] = u[x][y][time]
    n+=1

plt.grid("True")
plt.xlabel("Time[s]")
plt.ylabel("Temperature[C]")
plt.plot(t, T_ob, label="Measured")
plt.plot(t, T_nm, label="Numerical")
plt.legend()
plt.title("Comparison of Numerical and Measured Temperatures")
plt.savefig("figures/plot.png")

with open('heat_equation.txt', 'w') as file:
    file.write('')