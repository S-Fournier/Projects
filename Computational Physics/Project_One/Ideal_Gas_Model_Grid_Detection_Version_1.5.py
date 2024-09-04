import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

position_distribution = 'normal' #normal or uniform
velocity_distribution = 'maxwell-boltzman' #maxwell-boltzman or uniform
plot = 'animation' #animation,  entropy or pressure
save = 'no' #save the animation
file_name = 'test.gif'

N = 1000 #number of particles
wall = 10000 #box size
cell = 1000 #cell size
time_stop = 300 #number of steps

k_B = 1.38*10**(-23) #boltzmann constant (J/K)
m_H = 1.67*10**(-24) #mass of hydrogen (kg)
t_k = 300  #temperature (K)
v_th = np.sqrt(k_B * t_k/m_H)  #thermal velocity

if(position_distribution == 'normal'):
    
    sigma = 20
    x = np.random.normal(wall/2, sigma, N)
    y = np.random.normal(wall/2, sigma, N)

elif(position_distribution == 'uniform'):
    
    x = np.random.uniform(0, wall, N)
    y = np.random.uniform(0, wall, N)

mu = np.random.uniform(0, 1, N)

if(velocity_distribution == 'maxwell-boltzman'):

    v = v_th * np.sqrt(-2 * np.log(1 - mu))

elif(velocity_distribution=='uniform'):

    v = mu * cell

theta = np.random.uniform(0, 2 * np.pi, N)
vx = v * np.cos(theta) #velocity in x direction
vy = v * np.sin(theta) #velocity in y direction

s_record = np.zeros(time_stop)
p_record = np.zeros(time_stop)
x_record = np.zeros(shape = (N, time_stop))
y_record = np.zeros(shape = (N, time_stop))

id = np.arange(1, N + 1)
grid = np.zeros(shape=(wall, wall)) #the position grid where the particles place their id flags
grid_bins = np.zeros(shape = (int(wall/cell), int(wall/cell))) #the bins that particles correspond to in order to calculate entropy

def calculate_pressure(vx, vy, m):
    
    vmag = np.sqrt(vx**2 + vy**2)
    pressure = 2 * m * vmag
    
    return pressure

def calculate_entropy(grid_bins, s = 0):
    
    for i in range(10):
        
        for j in range(10):
            
            p = grid_bins[i, j]/N
            
            if(p > 0):
                
                s = s - p * np.log(p)
            
            p = 0

    return s

def wall_check(x, y, vx, vy, p_record, m, hit=False):
    
    a = x >= wall-1
    b = y >= wall-1
    c = x <= 0
    d = y <= 0

    if(a or c == True):
        
        hit = True
        vx = -vx
        x = x + vx
    
    if(b or d == True):
        
        hit = True
        vy = -vy
        y = y + vy
    
    if(hit == True):
        
        p_record = p_record + calculate_pressure(vx, vy, m)

        x, y, vx, vy, p_record = wall_check(x, y, vx, vy, p_record, m)

    return x, y, vx, vy, p_record

for t in range(time_stop):
    
    for i in range(N):

        x[i] = x[i] + vx[i]
        y[i] = y[i] + vy[i]

        x[i], y[i], vx[i], vy[i], p_record[t] = wall_check(x[i], y[i], vx[i], vy[i], p_record[t], m_H)
        
        grid[int(x[i]), int(y[i])] = grid[int(x[i]), int(y[i])] + id[i]
        grid_bins[int(x[i]/cell), int(y[i]/cell)] = grid_bins[int(x[i]/cell), int(y[i]/cell)] + 1
        
        if(grid[int(x[i]), int(y[i])] != id[i]):

            u = int(grid[int(x[i]), int(y[i])] - id[i]-1)

            vx[i], vx[u]=vx[u], vx[i]
            vy[i], vy[u]=vy[u], vy[i]

            grid[int(x[i]), int(y[i])] = 0

    if(plot=='entropy'):
        
        s_record[t] = calculate_entropy(grid_bins) 
    
    x_record[:, t] = x
    y_record[:, t] = y

    grid = np.zeros(shape = (wall, wall))
    grid_bins = np.zeros(shape = (wall, wall))

if(plot == 'animation'):
    
    fig = plt.figure()
    ax = plt.axes(xlim = (0- (wall/10), wall + (wall/10)), ylim=(0-(wall/10), wall+(wall/10)))
    plt.axis('off')
    rectangle = plt.Rectangle((0, 0), wall, wall, fc = 'white', ec = "red")
    plt.gca().add_patch(rectangle)
    dot, = ax.plot([], [], 'bo', ms = 1)

    def init():
        
        dot.set_data([], [])
        
        return dot, 

    def animate(i):
        
        x = x_record[:, i]
        y = y_record[:, i]
        dot.set_data(x,  y)
        
        return dot, 

    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = time_stop, interval = 200, blit = True)
    
    if(save == 'yes'):
        
        anim.save(file_name)

elif(plot == 'entropy'):

    time_axis = np.arange(0, time_stop)
    plt.plot(time_axis, s_record, '.', )
    plt.xlabel('Time (steps)')
    plt.title('Entropy vs Time')

elif(plot == 'pressure'):

    time_axis = np.arange(0, time_stop)
    plt.plot(time_axis, p_record, '.')

plt.show()