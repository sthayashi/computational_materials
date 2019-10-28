import matplotlib.pyplot as plt
import numpy as np

positions_velocities = np.loadtxt('positions_velocities.dat')
energies = np.loadtxt('energies.dat')

# For x(t) and v(t)
times = positions_velocities[:,0]
positions = positions_velocities[:,1]
velocities = positions_velocities[:,2]

# For Ekin, Epot, Etotal
kinetic_energies = energies[:,1]
potential_energies = energies[:,2]
total_energies = energies[:,3]

fig, axs = plt.subplots(5, figsize=(15,15))
axs[0].plot(times, positions)
axs[1].plot(times, velocities)
axs[2].plot(times, kinetic_energies)
axs[3].plot(times, potential_energies)
axs[4].plot(times, total_energies)
axs[0].set(ylabel="x(t)")
axs[1].set(ylabel="v(t)")
axs[2].set(ylabel="Kinetic Energy")
axs[3].set(ylabel="Potential Energy")
axs[4].set(ylabel="Total Energy")
axs[4].set(xlabel="Time")
plt.tight_layout()
plt.savefig("comps.pdf")
