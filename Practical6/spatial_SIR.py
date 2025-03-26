import numpy as np
import matplotlib.pyplot as plt

# Parameters
beta = 0.3
gamma = 0.05
timesteps = 100

# Initialize grid
population = np.zeros((100, 100))
outbreak = np.random.choice(100, 2)
population[outbreak[0], outbreak[1]] = 1

# Simulation loop
for t in range(timesteps):
    infected = np.argwhere(population == 1)
    new_infections = []
    
    # Infect neighbors
    for i, j in infected:
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < 100 and 0 <= nj < 100:
                    if population[ni, nj] == 0 and np.random.rand() < beta:
                        new_infections.append((ni, nj))
    
    # Apply new infections
    for ni, nj in new_infections:
        population[ni, nj] = 1
    
    # Recover infected individuals
    for i, j in infected:
        if np.random.rand() < gamma:
            population[i, j] = 2
    
    # Plot every 10 timesteps
    if t % 10 == 0:
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time Step {t}')
        plt.pause(0.1)

plt.show()
