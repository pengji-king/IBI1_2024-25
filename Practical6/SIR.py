# import some necessary  libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10000
beta = 0.3
gamma = 0.05
initial_infected = 1
timesteps = 1000

# Initial conditions
S = [N - initial_infected]
I = [initial_infected]
R = [0]

# Simulation loop
for _ in range(timesteps):
    current_S = S[-1]
    current_I = I[-1]
    
    # Calculate new infections and recoveries
    infection_prob = beta * current_I / N
    new_infections = np.random.binomial(current_S, infection_prob)
    new_recoveries = np.random.binomial(current_I, gamma)
    
    # Update compartments
    next_S = current_S - new_infections
    next_I = current_I + new_infections - new_recoveries
    next_R = R[-1] + new_recoveries
    
    # Ensure non-negative values
    S.append(max(next_S, 0))
    I.append(max(next_I, 0))
    R.append(max(next_R, 0))

# Plotting
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('Basic Stochastic SIR Model')
plt.legend()
plt.savefig('/Users/wangermi/Desktop/note/IBI1 8011/IBI1_2024-25/Practical6/SIR_plot.png')
plt.show()