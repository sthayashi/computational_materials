import numpy as np
import matplotlib.pyplot as plt
import csv
#For a known F(t), the EOM is:

#d^2/dr^2 (x(t)) * m = F(t)

# initialize constants
m = 1 # Mass
k = 1 # Spring constant
delta_t = 0.01 # Timestep
tf = 10.01 # Total time
xeq = 0.0 # Equilibrium length
x0 = 0.1 # Initial position
v0 = 0.3 # Initial velocity

# formulas
def take_step(x_t, v_t):
    x_t_new = x_t + v_t * delta_t
#   delta_x = x_t_new
#   Fs_t = -k*delta_x
    Fs_t = -k*x_t_new
    v_new_t = (1/m)*Fs_t*delta_t + v_t
    return x_t_new, v_new_t


positions = [x0]
velocities = [v0]
times = [0.00]
x = x0
v = v0
for t in np.arange(0.01, tf, 0.01):
    x, v = take_step(x, v)
    positions.append(x)
    velocities.append(v)
    times.append(t)


#fig, axs = plt.subplots(2)
#axs[0].plot(times, positions)
#axs[0].set_title("x(t)")
#axs[1].plot(times, velocities)
#axs[1].set_title("v(t)")
#plt.show()

# Store data. Whitespace delimited.

#data = zip(times, positions, velocities)
#with open('data.dat', 'w') as f:
#    f.write("Time \t Position \t Velocity\n")
#    writer = csv.writer(f, delimiter='\t')
#    writer.writerows(data)

#data2 = np.array([times, positions, velocities])
#data2 = data2.T
#print(data2)
#with open('data2.dat', 'w') as f:
#    np.savetxt(f, data2, fmt=['%d', '%d', '%d'])

np.savetxt('data2.dat', data2, header="Time    Positions    Velocities")
