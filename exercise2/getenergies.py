import numpy as np

data = np.loadtxt('positions_velocities.dat')
# k=m=1
times = []
KEs = []
PEs = []
Etots = []
for timeframe in data:
    t = timeframe[0]
    position = timeframe[1]
    velocity = timeframe[2]
    KE = 0.5*velocity*velocity
    PE = 0.5*position*position
    Etot = KE + PE
    times.append(t)
    KEs.append(KE)
    PEs.append(PE)
    Etots.append(Etot)

data = np.array([times, KEs, PEs, Etots])
data = data.T
np.savetxt('energies.dat', data, header="Time    Kinetic_Energy    Potential_Energy    Total_Energy")
