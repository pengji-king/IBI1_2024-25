import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10000
beta = 0.3
gamma = 0.05
initial_infected = 1
timesteps = 1000
vaccination_percentages = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

plt.figure(figsize=(6, 4), dpi=150)

for v in vaccination_percentages:
    vaccinated = int(N * v)
    S = [max(N - vaccinated - initial_infected, 0)]  # 防止负数
    I = [initial_infected]
    R = [vaccinated]

    for _ in range(timesteps):
        current_S = S[-1]
        current_I = I[-1]
        
        infection_prob = beta * current_I / N
        new_infections = np.random.binomial(current_S, infection_prob)
        new_recoveries = np.random.binomial(current_I, gamma)
        
        next_S = current_S - new_infections
        next_I = current_I + new_infections - new_recoveries
        next_R = R[-1] + new_recoveries
        
        S.append(max(next_S, 0))
        I.append(max(next_I, 0))
        R.append(max(next_R, 0))

    plt.plot(I, label=f'{int(v*100)}% Vaccinated')

plt.xlabel('Time')
plt.ylabel('Number of Infected')
plt.title('SIR Model with Vaccination')
plt.legend()
plt.savefig('SIR_vaccination_plot.png')
plt.show()